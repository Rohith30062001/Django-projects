from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('loginuser', views.login, name='login'),
]