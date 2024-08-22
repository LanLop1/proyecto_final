from django.db import models
from django.utils import timezone
from stores.models import Store


class Coupon(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    code = models.CharField(max_length=100, null=False)
    discounttype = models.TextField(max_length=1255, null=False)
    discountvalue = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    expirydate = models.DateField(null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return f"Code of discount, store and discount value: {self.code, self.store, self.discountvalue}"
    
# Create your models here.
