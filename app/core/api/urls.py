from core.api.views import TokenCheckAPIView, UserCreateAPIView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("auth-token/", obtain_auth_token, name="auth-token"),
    path("check-token/", TokenCheckAPIView.as_view(), name="check-token"),
]
