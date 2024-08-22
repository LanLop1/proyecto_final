# chat_support/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from a_users.models import Profile

@login_required
def chat_room(request, username):
    other_user = Profile.objects.get(user__username=username)
    messages = ChatMessage.objects.filter(
        sender__in=[request.user.profile, other_user],
        receiver__in=[request.user.profile, other_user]
    ).order_by('sentat')

    if request.method == 'POST':
        message_content = request.POST.get('message')
        ChatMessage.objects.create(
            sender=request.user.profile,
            receiver=other_user,
            messagecontent=message_content
        )
        return redirect('chat_room', username=username)

    return render(request, 'chat_support/chat.html', {
        'other_user': other_user,
        'messages': messages
    })

@login_required
def get_messages(request, username):
    other_user = Profile.objects.get(user__username=username)
    messages = ChatMessage.objects.filter(
        sender__in=[request.user.profile, other_user],
        receiver__in=[request.user.profile, other_user]
    ).order_by('sentat')

    message_list = [{
        'sender': message.sender.user.username,
        'messagecontent': message.messagecontent,
        'sentat': message.sentat.strftime('%Y-%m-%d %H:%M:%S')
    } for message in messages]

    return JsonResponse(message_list, safe=False)
