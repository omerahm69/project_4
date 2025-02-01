from django.contrib import admin
from . models import restaurant, Customer, MenuItem, Order, Reservation

# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display=('name','price','quantity')
    
admin.site.register (restaurant)
admin.site.register(Customer)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(Reservation)
