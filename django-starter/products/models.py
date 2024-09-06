from django.db import models
from django.utils import timezone
from stores.models import Store
from a_home.models import Image

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=1255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stockquantity = models.IntegerField(null=False)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, related_name='product_images')
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return f"Product name, price, store and stock: {self.name, self.price, self.store, self.stockquantity}"
