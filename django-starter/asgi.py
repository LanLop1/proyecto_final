import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat_support.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_starter.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat_support.routing.websocket_urlpatterns
        )
    ),
})
