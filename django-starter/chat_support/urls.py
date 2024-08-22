# chat_support/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chat/<str:username>/', views.chat_room, name='chat_room'),
    path('users/', views.user_list, name='user_list'),
]
