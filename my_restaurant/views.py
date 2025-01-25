from django.shortcuts import render
from my_restaurant import views as home_views
from django.http import HttpResponse
#from django.views import generic



# Create your views here.
def home_views(request):
        return HttpResponse(request, 'This is my home page')