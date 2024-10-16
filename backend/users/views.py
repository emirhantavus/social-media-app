from rest_framework import generics, permissions, status
from users.models import Account , Profile , Follow
from users.serializers import UserSerializer, RegisterSerializer, ProfileUpdateSerializer, LoginSerializer , FollowSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework import serializers
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from logs.models import IPLog
from django.utils import timezone

class RegisterView(generics.CreateAPIView):
      queryset = Account.objects.all()
      permission_classes = [permissions.AllowAny,]
      serializer_class = RegisterSerializer
      
      def perform_create(self, serializer):
            user = serializer.save()
            try:
                  Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                  Profile.objects.create(user=user)
            except IntegrityError:
                  raise serializers.ValidationError("Profile already exists.")
            
class UserList(APIView):
      def get(self,request):
            users = Account.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
            
            
class LoginView(APIView):
      permission_classes = [permissions.AllowAny,]
      
      def post(self,request):
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            
            user = authenticate(request, email=email,password=password)
            
            if user is not None:
                  ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                  ip_log, created = IPLog.objects.get_or_create(user=user, ip_address=ip_address)
                  if created:
                        ip_log.last_logged = timezone.now()
                        ip_log.save()
                        
                  refresh = RefreshToken.for_user(user)
                  return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                  },status.HTTP_200_OK)
            else:
                  return Response({'error':'Invalid credentials.'},status.HTTP_400_BAD_REQUEST)
            
class LogOutView(APIView):
      permission_classes = [permissions.IsAuthenticated]
      def post(self,request):
            try:
                  refresh_token = request.data.get("refresh")
                  token = RefreshToken(refresh_token)
                  token.blacklist()
                  return Response({'message':'Log out successfuly.'},status=status.HTTP_200_OK)
            except Exception as e:
                  return Response({'message':str(e)},status=status.HTTP_400_BAD_REQUEST)
            
class DeleteUserView(APIView):
      permission_classes = [permissions.IsAuthenticated]
      
      def delete(self,request):
            user = request.user
            user.delete()
            return Response({'message':'User deleted successfully.'},status=status.HTTP_200_OK)
            
class UserProfileView(generics.RetrieveUpdateAPIView):
      queryset = Profile.objects.all()
      serializer_class = ProfileUpdateSerializer
      permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
      
      def get_object(self):
            profile = Profile.objects.get(user=self.request.user)
            return profile
      
      def update(self,request,*args,**kwargs):
            profile = self.get_object()
            serializer = self.get_serializer(profile, data=request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
      
      
class FollowView(APIView):
      permission_classes = [permissions.IsAuthenticated]

      def post(self, request, user_id):
            follower = request.user
            following_user_id = user_id
            follow_instance, created = Follow.objects.get_or_create(
                follower=follower,
                following_id=following_user_id
            )     
            if created:
                return Response({'message': 'Followed successfully!'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'You are already following this user.'}, status=status.HTTP_400_BAD_REQUEST)
          
      def delete(self,request,user_id):
            follower = request.user
            following_user_id = user_id
            try:
                  follow_instance = Follow.objects.get(
                        follower=follower,
                        following_id = following_user_id
                  )
                  follow_instance.delete()
                  
                  return Response({'message':'Unfollowed successfully!'},status=status.HTTP_200_OK)
            except Follow.DoesNotExist:
                  return Response({'message':'You are not following this user.'})