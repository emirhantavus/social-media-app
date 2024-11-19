from notifications.models import Notification

def create_notification(user, message):
      if not user or not message:
            raise ValueError("User and message fields required.")
      
      Notification.objects.create(
            user=user,
            message=message
      )