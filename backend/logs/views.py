from django.shortcuts import render
from rest_framework import generics , permissions , status
from logs.models import IPLog , ActionLog
from logs.serializers import IPLogSerializers , ActionLogSerializers , UserAPIKeySerializer
from rest_framework_api_key.permissions import HasAPIKey
#from logs.permissions import IsAdminAndHasAPIKey
from rest_framework.views import APIView
from rest_framework.response import Response
from logs.models import UserAPIKey
from rest_framework_api_key.models import APIKey
from users.models import LoginAttempt


class ListIPLogsView(generics.ListAPIView):
      permission_classes = [HasAPIKey]
      queryset = IPLog.objects.all()
      serializer_class = IPLogSerializers
      
      
class ListActionLogsView(generics.ListAPIView):
      queryset = ActionLog.objects.all()
      serializer_class = ActionLogSerializers
      permission_classes = [HasAPIKey] ## IsAdmin ile degistirmeyi unutma sonra. !!
      
class GenerateAPIKey(APIView):
      permission_classes = [permissions.IsAuthenticated]
      def post(self,request):
            email = request.user.email
            check_email = UserAPIKey.objects.get(email=email)
            
            if not email:
                  return Response({'message':'Email is required.'},status=status.HTTP_401_UNAUTHORIZED)
            
            if check_email:
                  return Response({
                        'message':'U already have a key.',
                        'api_key':check_email.api_key
                        }, status=status.HTTP_200_OK)
            
            api_key, key = APIKey.objects.create_key(name=email)
            UserAPIKey.objects.create(email=email,api_key=key)
            
            return Response({'api_key':key},status=status.HTTP_200_OK)
      
class RetrieveAPIKey(APIView):
      permission_classes = [permissions.IsAuthenticated]
      def get(self, request):
            email = request.user.email
            
            try:
                  user_api_key = UserAPIKey.objects.get(email=email)
                  return Response({'email':user_api_key.email,'api_key':user_api_key.api_key},status=status.HTTP_200_OK)
            
            except UserAPIKey.DoesNotExist:
                  return Response({'message':'API key not found for this email.'},status=status.HTTP_404_NOT_FOUND)
            
class ListAllAPIKey(APIView):
      permission_classes = [permissions.IsAdminUser]
      
      def get(self,request):
            keys = UserAPIKey.objects.all()
            serializer = UserAPIKeySerializer(keys,many=True)
            return Response({'keys':serializer.data},status=status.HTTP_200_OK)
            
class DeleteAPIkey(APIView):
      permission_classes = [permissions.IsAdminUser]
      
      def post(self,request):
            key_id = request.data.get('id')
            
            if not key_id:
                  return Response({'message':'Key id is required'},status=status.HTTP_400_BAD_REQUEST)
            
            try:
                  api_key = UserAPIKey.objects.get(id=key_id)        
            except:
                  return Response({'message':'Key id not found'},status=status.HTTP_404_NOT_FOUND)
            
            api_key.delete()
            return Response({'message':'API key deleted successfully'},status=status.HTTP_200_OK)
      
class ListAllAttempts(generics.ListAPIView):
      permission_classes = [permissions.IsAdminUser]
      queryset = LoginAttempt.objects.all()