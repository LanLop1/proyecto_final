from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    nombre = models.CharField(max_length=200, null = False)
    apellido = models.CharField(max_length=200, null = False)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True) 
    email = models.EmailField(max_length= 50)
    phone = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return str(self.user)
    
    @property
    def name(self):
        if self.displayname:
            return self.displayname
        return self.user.username 
    
    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return static("images/avatar.svg")

class SubscriptionPlan(models.Model):
    planname = models.CharField(max_length=200, null=False, unique=True)
    storagelimit = models.IntegerField(null=False)
    features = models.TextField(max_length=1255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)


class UserSubscription(models.Model):
    usuario = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE, null=False)
    startdate = models.DateField(null=False)
    enddate = models.DateField(null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)


'''
from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

class Profile(models.Model):
    name = models.CharField(max_length=200, null=False)
    apellido = models.CharField(max_length=400, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True) 
    email = models.EmailField(max_length= 50)
    
    
    def __str__(self):
        return str(self.user)
    
    @property
    def name(self):
        if self.displayname:
            return self.displayname
        return self.user.username 
    
    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return static("images/avatar.svg")
'''