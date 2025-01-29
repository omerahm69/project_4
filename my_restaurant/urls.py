
from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('home/', views.about_us, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('booking/', views.about_us, name='booking'),
    path('menu/', views.about_us, name='menu'),
    path('contact_us/', views.about_us, name='contact_us'),
    
]
