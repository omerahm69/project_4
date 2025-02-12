from django.shortcuts import render, redirect
from . models import MenuItem, Order
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import MenuItem as Menu
#from django.views import generic

# Create your views here.

def home(request):
        Menu.objects.all()
        specials=MenuItem.objects.all()[:3]
        return render(request, 'my_restaurant/home.html', {'specials': specials})

def about_us(request):
        return render(request, 'my_restaurant/about_us.html')

def menu(request):
        items=MenuItem.objects.all()
        return render(request, 'my_restaurant/menu.html',{'items':items})

def booking(request):
        return render(request, 'my_restaurant/booking.html')

def contact_us(request):
        if request.method =='POST':
                name=request.POST['name']
                email=request.POST['email']
                message=request.POST['message']
                messages.success(request,'Your message has been submitted!')
                return redirect('contact_us')
        return render(request, 'my_restaurant/contact_us.html')
def user_login(request):
        if request.method=='POST':
                username=request.POST['username']
                password=request.POST['password']
                user=authenticate(request, username=username, password=password)
                if user is not None:
                        login(request,user)
                        return redirect('home')
                else:
                        messages.error(request, 'invalid username or password')
        return render(request, 'my_restaurant/login.html')
def register(request):
        if request.method=='POST':
                username=request.POST['username']
                email=request.POST['email']
                password=request.POST['password']
                confirm_password=request.POST['confirm_password']
                if password==confirm_password:
                        if User.objects.filter(username).exists():
                                messages.error(request,'Username already exist.')
                        elif User.objects.filter(email=email).exists():
                                messages.error(request,'Email already registered.')
                        else:
                                user=User.objects.create_user(username=username, email=email, password=password)
                                user_login(request, user)
                                return redirect('home')
                                messages.error(request, 'Passwords do not match.')
                        return render(request, 'register.html')
def menu(request):
        menu_items = MenuItem.objects.all()
        return render(request, 'my_restaurant/menu.html', {'menu_items': MenuItem})

