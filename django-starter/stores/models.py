from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from a_home.models import Template, Image

class Store(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    template = models.ForeignKey(Template, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=1255, null=False)
    horario = models.TextField(max_length=1255,null=True)  # Changed to allow null
    dirección = models.TextField(max_length=1255,null=True)  # Changed to allow null
    imageStore= models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, related_name='stores_images')
    logoImage= models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, related_name='stores_logo_images')
    bannerImage= models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, related_name='stores_banner_images')
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return f"Store name and owner: {self.name, self.owner}"

class QRCode(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, related_name='qr_codes')
    createdat = models.DateTimeField(default=timezone.now)