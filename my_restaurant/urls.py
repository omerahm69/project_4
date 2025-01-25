
from django.urls import path
from my_restaurant.views import home
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    
]
