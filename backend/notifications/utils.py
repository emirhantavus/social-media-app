from notifications.models import Notification
from notifications.tasks import send_email_notification
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def create_notification(user, message):
      if not user or not message:
            raise ValueError("User and message fields required.")
      
      Notification.objects.create(
            user=user,
            message=message
      )
      
      send_email_notification.delay(user.email, "New Notification",message)
      
      ###websocket
      
      channel_layer = get_channel_layer()
      group_name = f"user_{user.id}"
      async_to_sync(channel_layer.group_send)(
            group_name,
            {
                  "type":"notification_message",
                  "message":message,
            }
      )