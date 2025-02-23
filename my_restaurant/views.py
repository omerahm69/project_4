from django.shortcuts import render, redirect
from . models import MenuItem, Order
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.db import models
from .models import MenuItem as Menu
from django.contrib import messages
from django.contrib.auth import views as auth_views

# Create your views here.

def home(request):
        Menu.objects.all()
        specials=Menu.objects.all()[:3]
        return render(request, 'my_restaurant/home.html', {'specials': specials})

def about_us(request):
        return render(request, 'my_restaurant/about_us.html')

def menu(request):
        menu_items=MenuItem.objects.all()
        return render(request, 'my_restaurant/menu.html',{'menu_items':menu_items})

def booking(request):
        return render(request, 'my_restaurant/booking.html')

def contact_us(request):
        if request.method =='POST':
                name=request.POST.get('name')
                email=request.POST.get ('email')
                message=request.POST.get('message')
                messages.success(request,'Your message has been submitted!')
                return redirect('contact_us')
        return render(request, 'my_restaurant/contact_us.html')
def login_register_view(request):
      
        if request.method == "POST":
                username = request.POST.get("username")
                password = request.POST.get("password")

                user = authenticate(request, username=username, password=password)  # Authenticate user
                if user is not None:
                        login(request, user)
                        return redirect("home")
                else:
                        return render(request, "user_login.html", {"error": "Invalid credentials"})
                
        return render(request, "my_restaurant/login.html")

def register(request):
        form=UserCreationForm()
        return render(request, 'my_restaurant/login.html', {"form":form})

def menu(request):
        menu_items = MenuItem.objects.all()
        return render(request, 'my_restaurant/menu.html', {'menu_items': menu_items})


