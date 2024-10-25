from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class IPLog(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      ip_address = models.GenericIPAddressField()
      last_logged = models.DateTimeField(default=timezone.now)
    
      def __str__(self):
            return f'{self.user.email} - {self.ip_address}'


class ActionLog(models.Model):
      ACTION_CHOICES = [
          ('CREATE', 'Create'),
          ('UPDATE', 'Update'),
          ('DELETE', 'Delete'),
      ]

      user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='action_logs')
      action = models.CharField(max_length=10, choices=ACTION_CHOICES)
      model_name = models.CharField(max_length=50)
      object_id = models.PositiveIntegerField()
      timestamp = models.DateTimeField(auto_now_add=True)
      detail = models.TextField(blank=True, null=True)

      def __str__(self):
          return f"{self.user.email} performed {self.action} on {self.model_name} at {self.timestamp}"
      
      
class UserAPIKey(models.Model):
    email = models.EmailField()
    api_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.email} - {self.api_key}"