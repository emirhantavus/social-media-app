from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class IPLog(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      ip_address = models.GenericIPAddressField()
      last_logged = models.DateTimeField(default=timezone.now)
    
      def __str__(self):
            return f'{self.user.username} - {self.ip_address}'
