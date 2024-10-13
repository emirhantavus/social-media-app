from django.shortcuts import render
from rest_framework import generics , permissions
from logs.models import IPLog , ActionLog
from logs.serializers import IPLogSerializers , ActionLogSerializers

class ListIPLogsView(generics.ListAPIView):
      queryset = IPLog.objects.all()
      serializer_class = IPLogSerializers
      
      
class ListActionLogsView(generics.ListAPIView):
      queryset = ActionLog.objects.all()
      serializer_class = ActionLogSerializers
      permission_classes = [permissions.IsAuthenticated] ## IsAdmin ile degistirmeyi unutma sonra. !!