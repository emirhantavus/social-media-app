from django.shortcuts import render
from notifications.models import Notification
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class NotificationListView(APIView):
      permission_classes = [permissions.IsAuthenticated]
      
      def get(self, request):
            notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
            data = [
                  {
                        "id":n.id,
                        "message":n.message,
                        "created_at":n.created_at,
                        "is_read":n.is_read
                  }
                  for n in notifications
            ]
            return Response(data)