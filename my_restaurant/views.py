from django.shortcuts import render
from django.http import HttpResponse
#from django.views import generic



# Create your views here.
def home(request):
        return render(request, 'my_restaurant/home.html')

def about_us(request):
        return render(request, 'my_restaurant/about_us.html')

