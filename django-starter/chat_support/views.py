# chat_support/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from a_users.models import Profile
from django.http import JsonResponse

@login_required
def user_list(request):
    users = Profile.objects.exclude(user=request.user).values('user__username')
    return JsonResponse({'users': list(users)})

@login_required
def chat_room(request, username):
    receiver = Profile.objects.get(user__username=username)
    room_name = f'{request.user.username}_{receiver.user.username}'
    return render(request, 'chat_support/chat.html', {
        'room_name': room_name,
        'receiver_username': username
    })
