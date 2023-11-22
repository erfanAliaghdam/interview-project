from django.urls import path
from core.api.v1.views import (
    CustomTokenObtainPairView,
    CustomRefreshTokenView,
    register_client_user_view
)

urlpatterns = [
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token-create'),
    path('auth/token/refresh/', CustomRefreshTokenView.as_view(), name='token-refresh'),

    path('auth/register/client/', register_client_user_view, name='register-client')
]
