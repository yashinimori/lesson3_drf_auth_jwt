from django.contrib import admin
from django.urls import path, include
from .views import RegistrationView, LoginView, UserView

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('', UserView.as_view(), name='users')
]
