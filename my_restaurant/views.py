from django.shortcuts import render
from . models import restaurant
from . models import MenuItem


#from django.views import generic



# Create your views here.

def home(request):
        return render(request, 'my_restaurant/home.html')
        Restaurant= restaurant.objects.all()
def about_us(request):
        return render(request, 'my_restaurant/about_us.html')

def menu(request):
        return render(request, 'my_restaurant/menu.html')

def booking(request):
        return render(request, 'my_restaurant/booking.html')

def contact(request):
        return render(request, 'my_restaurant/contact_us.html')

def login(request):
        return render(request, 'my_restaurant/login.html')


def menu_view(request):
        menu_items = MenuItem.objects.all()
        return render(request, 'restaurant/menu.html', {'menu_items': menu_items})

