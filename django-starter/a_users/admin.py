from django.contrib import admin
from .models import Profile, SubscriptionPlan, UserSubscription

admin.site.register(Profile)
admin.site.register(SubscriptionPlan)
admin.site.register(UserSubscription)
