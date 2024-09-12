from django.urls import path
from .views import notification_list, check_new_notifications, mark_notification_as_read, mark_all_notifications_as_read

urlpatterns = [
    path('notifications/', notification_list, name='notification_list'),
    path('check_new_notifications/', check_new_notifications, name='check_new_notifications'),
    path('mark_notification_as_read/<int:notification_id>/', mark_notification_as_read, name='mark_notification_as_read'),
    path('mark_all_notifications_as_read/', mark_all_notifications_as_read, name='mark_all_notifications_as_read'),
]
