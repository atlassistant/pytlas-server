from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views, consumers

urlpatterns = [
  path('', views.index),
  path('api/', views.api_index),
  path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

websocket_urlpatterns = [
  path('ws/assistant/', consumers.AssistantConsumer),
]