# chat_support/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessage
from a_users.models import Profile
from django.utils import timezone

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender_username = text_data_json['sender']

        # Guarda el mensaje en la base de datos
        sender = await self.get_user(sender_username)
        receiver_username = self.room_name.replace(sender_username, "").replace("_", "")
        receiver = await self.get_user(receiver_username)

        chat_message = ChatMessage.objects.create(
            sender=sender,
            receiver=receiver,
            messagecontent=message,
            sentat=timezone.now()
        )

        # Enviar el mensaje a la sala de chat
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender_username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Enviar el mensaje al WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))

    @sync_to_async
    def get_user(self, username):
        return Profile.objects.get(user__username=username)
