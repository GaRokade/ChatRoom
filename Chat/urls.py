from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('', views.messages_page, name='messages_page'),  # Root of Chat app
]
