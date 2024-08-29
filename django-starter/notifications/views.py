# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from chat_support.models import Notification

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(
        usuario=request.user.profile,
        readstatus=b'\x00'  # Solo no leídas
    ).order_by('-createdat')

    # Convertir el BinaryField a un texto adecuado para la plantilla
    for notification in notifications:
        notification.readstatus_text = 'unread' if notification.readstatus == b'\x00' else 'read'
        
        # Extraer el nombre del usuario del mensaje
        message_parts = notification.message.split(': ', 1)
        if len(message_parts) > 1:
            notification.sender_username = message_parts[0].split('de ', 1)[-1]  # Obtener el nombre del usuario
        else:
            notification.sender_username = 'unknown'

    unread_count = notifications.filter(readstatus=b'\x00').count()
    
    return render(request, 'notifications/notification_list.html', {
        'notifications': notifications,
        'unread_count': unread_count
    })

@login_required
def check_new_notifications(request):
    unread_count = Notification.objects.filter(
        usuario=request.user.profile,
        readstatus=b'\x00'
    ).count()
    return JsonResponse({'unread_count': unread_count})

@csrf_exempt
@login_required
def mark_notification_as_read(request, notification_id):
    if request.method == 'POST':
        try:
            notification = Notification.objects.get(id=notification_id, usuario=request.user.profile)
            notification.readstatus = b'\x01'  # Marcar como leído
            notification.save()
            return JsonResponse({'status': 'success'})
        except Notification.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Notificación no encontrada'})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'})

@login_required
@require_POST
def mark_all_notifications_as_read(request):
    notifications = Notification.objects.filter(usuario=request.user.profile, readstatus=b'\x00')
    notifications.update(readstatus=b'\x01')  # Marcar todas como leídas
    return JsonResponse({'status': 'success'})