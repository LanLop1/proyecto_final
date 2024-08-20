from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=1255, null=True, blank=True)

    def __str__(self):
        return f"Image: {self.file.name}"
    
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=1255, null=True, blank=True)

    def __str__(self):
        return f"Image: {self.file.name}"
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=8000)
    content = models.TextField(max_length=8000)
    resumen = models.TextField(max_length=1255)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
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

class User(models.Model):
    name = models.CharField(max_length=200, null=False)
    apellido = models.CharField(max_length=400, null=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=128, null=False) 
    phone = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"User email: {self.email}"

    def set_password(self, raw_password):
        """Hash the password and store it."""
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        """Check the password against the stored hash."""
        return check_password(raw_password, self.password)
    
class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    template = models.ForeignKey(Template, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=1255, null=False)
    logourl = models.TextField(max_length=1255,null=True)  # Changed to allow null
    bannerurl = models.TextField(max_length=1255,null=True)  # Changed to allow null
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return f"Store name and owner: {self.name, self.owner}"

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

class SubscriptionPlan(models.Model):
    planname = models.CharField(max_length=200, null=False, unique=True)
    storagelimit = models.IntegerField(null=False)
    features = models.TextField(max_length=1255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE, null=False)
    startdate = models.DateField(null=False)
    enddate = models.DateField(null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
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

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    message = models.TextField(max_length=8000, null=False)
    readstatus = models.BinaryField(null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', null=False)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', null=False)
    messagecontent = models.TextField(max_length=8000, null=False)
    sentat = models.DateTimeField(default=timezone.now)

class QRCode(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, related_name='qr_codes')
    createdat = models.DateTimeField(default=timezone.now)

class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    issuedate = models.DateField(null=False)
    duedate = models.DateField(null=False)
    totalamount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.TextField(max_length=1255, null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

