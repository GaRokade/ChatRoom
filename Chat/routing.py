from django.urls import path
from . import consumers

websocket_urlpatterns=[
    path('Chat/',consumers.ChatConsumer.as_asgi()),
]