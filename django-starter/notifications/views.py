from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chat_support.models import Notification

@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(usuario=request.user.profile, readstatus=b'\x00')
    # Marca notificaciones como leídas cuando se visualizan
    notifications.update(readstatus=b'\x01')
    return render(request, 'notifications/notifications.html', {'notifications': notifications})
