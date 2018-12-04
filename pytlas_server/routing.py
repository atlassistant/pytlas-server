from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from assistant.urls import websocket_urlpatterns

application = ProtocolTypeRouter({
  # Empty for now (http->django views is added by default)
  'websocket': AuthMiddlewareStack(
    URLRouter(
      websocket_urlpatterns,
    ),
  ),
})
