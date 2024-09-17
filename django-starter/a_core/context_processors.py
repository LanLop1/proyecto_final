from django.conf import settings
from chat_support.models import Notification

def notifications_context(request):
    if request.user.is_authenticated:
        unread_count = Notification.objects.filter(
            usuario=request.user.profile,
            readstatus=b'\x00'
        ).count()
    else:
        unread_count = 0

    return {
        'unread_count': unread_count
    }
