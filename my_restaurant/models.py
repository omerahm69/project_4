from django.db import models
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(default='3')
    price= models.FloatField()
    quantity=models.IntegerField()
    image=models.CharField(max_length=2083, default='default.jpg')
    banner=models.ImageField(default=(''), blank=True)


class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    quantity=models.IntegerField(default=0)
    image = models.ImageField(upload_to='menu_images/', default='menu_images/default.jpg', null=True, blank=True)
    banner=models.ImageField(default=(''), blank=True)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    items=models.ManyToManyField(MenuItem)
    status=models.CharField(max_length=50, choices=[('pending','Pending'), ('completed','Completed'), ('cancelled','Cancelled')],default='pending')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order#{self.id} for{self.customer.name})"
    
class Reservation(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    date=models.DateTimeField()
    number_of_people=models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.customer.name} on {self.date}"