from notifications.models import Notification
from notifications.tasks import send_email_notification

def create_notification(user, message):
      if not user or not message:
            raise ValueError("User and message fields required.")
      
      Notification.objects.create(
            user=user,
            message=message
      )
      
      send_email_notification.delay(user.email, "New Notification",message)