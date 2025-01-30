from django.shortcuts import render

#from django.views import generic



# Create your views here.

def home(request):
        return render(request, 'my_restaurant/home.html')

def about_us(request):
        return render(request, 'my_restaurant/about_us.html')

def menu(request):
        return render(request, 'my_restaurant/menu.html')

def booking(request):
        return render(request, 'my_restaurant/booking.html')

def contact(request):
        return render(request, 'my_restaurant/contact_us.html')



