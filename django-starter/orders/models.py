from django.db import models
from a_users.models import Profile
from stores.models import Store
from django.utils import timezone
from products.models import Product

class Cart(models.Model):
    usuario = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
class Order(models.Model):
    usuario = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    totalamount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    orderstatus = models.TextField(max_length=1255,null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    issuedate = models.DateField(null=False)
    duedate = models.DateField(null=False)
    totalamount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.TextField(max_length=1255, null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

# Create your models here.
