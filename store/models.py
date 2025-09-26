from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Promotion(models.Model):
    discount = models.FloatField()
    description = models.CharField(max_length=255)
class Collection(models.Model):
    title = models.CharField(max_length=255)
    
class Product(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField()
    description =models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


    title = models.CharField(max_length=255)
    
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
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    
class Order(models.Model):
    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
        ('Failde', 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(choices=PAYMENT_STATUS)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete= models.PROTECT)
    product = models.ForeignKey(Product,  on_delete= models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits= 6, decimal_places= 2)
    

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.PositiveSmallIntegerField()