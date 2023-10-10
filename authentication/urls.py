from .views import UsernameValidationView, EmailValidationView, VerificationView, LoginView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('register', views.register_user, name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', views.logout_view, name="logout"),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name='validate_email'),
    path('activate/<uidb64>/<token>',
         VerificationView.as_view(), name='activate'),
]
