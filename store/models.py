from django.db import models
from django.contrib.auth import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length= 255)
    description =models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    
class Customer(models.Model):
    MEMBERSHIP_CHOICES =[
        ('B','Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField( null=True)
    membership = models.CharField(choices=MEMBERSHIP_CHOICES )
    
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    
class Order(models.Model):
    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
        ('Failde', 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(choices=PAYMENT_STATUS)