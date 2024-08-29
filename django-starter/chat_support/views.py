# chat_support/views.py
import json
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import ChatMessage, Notification
from a_users.models import Profile, User

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
        
        return JsonResponse({'status': 'success'})  # Cambia la respuesta a JSON

    return render(request, 'chat_support/chat.html', {
        'other_user': other_user,
        'messages': messages
    })

@login_required
@csrf_exempt
def update_user_status(request, username):
    if request.method == 'POST':
        status = request.POST.get('status')
        user_key = f"user_status_{request.user.username}"

        if status == 'online':
            cache.set(user_key, 'online', timeout=300)  # El estado se mantiene durante 5 minutos (300 segundos)
        else:
            cache.set(user_key, 'offline')

        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'failed'}, status=400)

@login_required
def check_user_status(request, username):
    user_key = f"user_status_{username}"
    status = cache.get(user_key, 'offline')
    return JsonResponse({'status': status})

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

def user_list(request):
    users = User.objects.exclude(username=request.user.username)  # Excluye al usuario actual
    return render(request, 'chat_support/user_list.html', {
        'users': users
    })