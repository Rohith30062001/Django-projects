from django.urls import path

from . import views     # it means - 'from all import views'

urlpatterns = [
    path('',views.login, name='index'),
    path('loginuser',views.login, name='index'),
    path('register',views.register, name='index'),
    path('loginperson',views.loginperson, name='index'),
    path('home',views.home, name='index'),
    path('logout',views.logout, name='logout'),
    path('book',views.book, name='book'),
    path('viewbookings',views.viewBookings, name='book'),
]
