from django.db import models
from django.utils import timezone
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    resumen = models.TextField(max_length=1255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Título: {self.title}"


class Template(models.Model):
    name = models.TextField(null=False)
    description = models.TextField(null=False)
    thumbnailurl = models.TextField(null=True)  # Changed to allow null
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    premium = models.BooleanField(null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

class User(models.Model):
    name = models.TextField(null=False)
    email = models.TextField(null=False)
    password = models.TextField(null=False)
    phone = models.TextField(null=False)
    address = models.TextField(null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    template = models.ForeignKey(Template, on_delete=models.CASCADE, null=False)
    name = models.TextField(null=False)
    description = models.TextField(null=False)
    logourl = models.TextField(null=True)  # Changed to allow null
    bannerurl = models.TextField(null=True)  # Changed to allow null
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    name = models.TextField(null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stockquantity = models.IntegerField(null=False)
    imageurl = models.TextField(null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

class Coupon(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    code = models.TextField(null=False)
    discounttype = models.TextField(null=False)
    discountvalue = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    expirydate = models.DateField(null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

class SubscriptionPlan(models.Model):
    planname = models.TextField(null=False)
    storagelimit = models.IntegerField(null=False)
    features = models.TextField(null=False)
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
    orderstatus = models.TextField(null=False)
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
    message = models.TextField(null=False)
    readstatus = models.TextField(null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', null=False)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', null=False)
    messagecontent = models.TextField(null=False)
    sentat = models.DateTimeField(default=timezone.now)

class QRCode(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    qrcodeurl = models.TextField(null=False)
    createdat = models.DateTimeField(default=timezone.now)

class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    issuedate = models.DateField(null=False)
    duedate = models.DateField(null=False)
    totalamount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.TextField(null=False)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)