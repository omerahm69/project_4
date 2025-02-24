
from django.urls import path, include
from django.contrib import admin
from. import views
from . views import login_register_view
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('menu/', views.menu, name='menu'),
    path('booking/', views.booking, name='booking'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('login/', login_register_view, name = 'login '),
    path('', include("django.contrib.auth.urls")),
    path('register/', views.register_user, name='register'),
    ]
