# chat_support/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chat/<str:username>/', views.chat_room, name='chat_room'),
    path('chat/<str:username>/messages/', views.get_messages, name='get_messages'),
    path('users/', views.user_list, name='user_list'),
    path('get_messages/<str:username>/', views.get_messages, name='get_messages'),
    path('update-status/<str:username>/', views.update_user_status, name='update_user_status'),
    path('check-status/<str:username>/', views.check_user_status, name='check_user_status'),
]
