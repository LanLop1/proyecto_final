from django.db import models
from a_users.models import Profile
from django.utils import timezone


class Notification(models.Model):
    usuario = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    message = models.TextField(max_length=8000, null=False)
    readstatus = models.BinaryField(null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

class ChatMessage(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_messages', null=False)
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_messages', null=False)
    messagecontent = models.TextField(max_length=8000, null=False)
    sentat = models.DateTimeField(default=timezone.now)

