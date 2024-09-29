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
                  refresh = RefreshToken.for_user(user)
                  return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                  },status.HTTP_200_OK)
            else:
                  return Response({'error':'Invalid credentials.'},status.HTTP_400_BAD_REQUEST)
            
class UserProfileView(generics.RetrieveUpdateAPIView):
      queryset = Profile.objects.all()
      serializer_class = ProfileUpdateSerializer
      permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
      
      def get_object(self):
            profile = Profile.objects.get(user__id=self.kwargs['pk'])
            return profile
      
      def update(self,request,*args,**kwargs):
            profile = self.get_object()
            if profile.user != request.user:
                  raise PermissionDenied('You can only update your own profile.')
            return super().update(request, *args , **kwargs)
      
      
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