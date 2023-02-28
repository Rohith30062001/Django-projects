from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='Rohith'),
    path('rohith', views.second, name='Rohith'),
    path('insert', views.insert, name='insert'),
    path('read', views.readData, name='readData'),
]