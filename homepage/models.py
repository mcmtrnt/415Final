from django.db import models
from decimal import Decimal
from datetime import datetime, timezone


class Ad(models.Model):
    ksl_id = models.TextField(null=True)
    displayTime = models.DateTimeField(null=True, default=None)
    category = models.TextField()
    subCategory = models.TextField()
    price = models.DecimalField(null=True, max_digits=9, decimal_places=2, default=Decimal(0))
    title = models.TextField()
    description = models.TextField(null=True)
    year = models.IntegerField(null=True)
    brand = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    name = models.TextField(null=True)
    cellPhone = models.TextField(null=True)
    size = models.IntegerField(null=True)
    favorited = models.TextField(null=True)
    kbb_value = models.TextField(null=True)
    make = models.TextField(null=True)
    model = models.TextField(null=True)
    difference = models.DecimalField(null=True, max_digits=7, decimal_places=2, default=Decimal(0))
    email = models.TextField(null=True)


class RecentAds(models.Model):
    ksl_id = models.TextField(null=True)
    displayTime = models.DateTimeField(null=True, default=None)
    category = models.TextField()
    subCategory = models.TextField()
    price = models.DecimalField(null=True, max_digits=9, decimal_places=2, default=Decimal(0))
    title = models.TextField()
    description = models.TextField(null=True)
    year = models.IntegerField(null=True)
    brand = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    name = models.TextField(null=True)
    cellPhone = models.TextField(null=True)
    size = models.IntegerField(null=True)
    favorited = models.TextField(null=True)
    kbb_value = models.TextField(null=True)
    make = models.TextField(null=True)
    model = models.TextField(null=True)
    difference = models.DecimalField(null=True, max_digits=7, decimal_places=2, default=Decimal(0))
    email = models.TextField(null=True)

class Pros(models.Model):
    user_id = models.TextField(null=True, default=None) 
    stripe_customer_id = models.TextField(null=True, default=None)
    charge_id = models.TextField(null=True, default=None) 
    subscription_id = models.TextField(null=True, default=None)
    
class Subscription(models.Model):
    product_id = models.TextField(null=True, default=None)
    plan_id = models.TextField(null=True, default=None)
    

