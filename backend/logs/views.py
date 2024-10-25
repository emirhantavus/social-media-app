from django.shortcuts import render
from rest_framework import generics , permissions , status
from logs.models import IPLog , ActionLog
from logs.serializers import IPLogSerializers , ActionLogSerializers
from rest_framework_api_key.permissions import HasAPIKey
#from logs.permissions import IsAdminAndHasAPIKey
from rest_framework.views import APIView
from rest_framework.response import Response
from logs.models import UserAPIKey
from rest_framework_api_key.models import APIKey

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
            
            if not email:
                  return Response({'message':'Email is required.'},status=status.HTTP_401_UNAUTHORIZED)
            
            api_key, key = APIKey.objects.create_key(name=email)
            UserAPIKey.objects.create(email=email,api_key=key)
            
            return Response({'api_key':key},status=status.HTTP_200_OK)