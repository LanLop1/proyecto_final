from django.contrib import admin
from .models import Article, Template, User, Store, Product, Coupon

admin.site.register(Article)
admin.site.register(Template)
admin.site.register(User)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Coupon)
