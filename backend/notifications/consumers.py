from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
      async def connect(self):
            self.group_name = f"user_{self.scope['user'].id}"
            if self.scope['user'].is_authenticated:
                  print(f"User connected: {self.scope['user'].id}")
                  await self.channel_layer.group_add(self.group_name, self.channel_name)
                  await self.accept()
            else:
                  print("User is not authenticated.!")
                  await self.close()
            
      async def disconnect(self, code):
            if self.scope['user'].is_authenticated:
                  await self.channel_layer.group_discard(self.group_name,self.channel_name)
            
      async def send_notification(self, event):
            await self.send(text_data=json.dumps({
                  'notification': event['message']
            }))