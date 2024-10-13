from django.shortcuts import render
from rest_framework import generics
from logs.models import IPLog
from logs.serializers import IPLogSerializers

class ListIPLogsView(generics.ListAPIView):
      queryset = IPLog.objects.all()
      serializer_class = IPLogSerializers