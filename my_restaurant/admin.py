from django.contrib import admin
from . models import restaurant

# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display=('name','price','quantity')
    
admin.site.register (restaurant)
