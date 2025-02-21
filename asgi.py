import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import studio.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kundalini_yoga.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            studio.routing.websocket_urlpatterns
        )
    ),
})
