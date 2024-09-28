from rest_framework import generics, permissions, status
from users.models import Account , Profile
from users.serializers import UserSerializer, RegisterSerializer, ProfileUpdateSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

class RegisterView(generics.CreateAPIView):
      queryset = Account.objects.all()
      permission_classes = [permissions.AllowAny,]
      serializer_class = RegisterSerializer
      
      def perform_create(self, serializer):
            user = serializer.save()
            Profile.objects.create(user=user)
      
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
      queryset = Account.objects.all()
      serializer_class = ProfileUpdateSerializer
      permission_classes = [permissions.IsAuthenticated]
      
      def get_object(self):
            return self.request.user