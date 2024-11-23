from channels.consumer import AsyncConsumer
from django.contrib.auth import get_user_model

User=get_user_model()

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected',event)
        
    async def websocket_receive(self, event):
        print('received',event)
  
    async def websocket_disconnect(self, event):
        print('disconnected',event)