from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(User, related_name="user_image", on_delete=models.CASCADE, null=True, blank=True)
    file = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=1255, null=True, blank=True)

    def __str__(self):
        return f"Image: {self.file.name}"
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=8000)
    resumen = models.TextField(max_length=1255)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Título: {self.title}"


class Template(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=1255, null=False)
    thumbnailurl = models.TextField(max_length=1255,null=True)  # Changed to allow null
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    premium = models.BooleanField(null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"Nombre: {self.name}"
    




