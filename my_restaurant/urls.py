
from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('menu/', views.menu, name='menu'),
    path('booking/', views.booking, name='booking'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('user_login/', views.user_login, name='login'),
    path('accounts/register/', views.register, name='register'),
    
    
]
