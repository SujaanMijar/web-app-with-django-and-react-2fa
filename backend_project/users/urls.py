from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login_view),
    path('mfa/setup/', views.mfa_setup),
    path('mfa/verify/', views.mfa_verify),
    path('mfa/login-verify/', views.mfa_login_verify),
    path('token/refresh/', TokenRefreshView.as_view()),
]