from django.conf import settings
from django_mako_plus import view_function, jscontext
from bs4 import BeautifulSoup
import requests
from homepage import models as hmod
import re
from datetime import datetime, timedelta  
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import time
from decimal import Decimal
from django.contrib.auth.models import User
from django.contrib.auth import models as pmod
import stripe


@view_function
def process_request(request):

    #print(request.user.id)

    # g1 = pmod.Group()
    # g1.name = "Pro"
    # g1.save()

    # g1= pmod.Group.objects.get(name='Pro')
    # g1.permissions.add(pmod.Permission.objects.get(codename='view_ad'))
    # g1.permissions.add(pmod.Permission.objects.get(codename='view_doctor'))
    # g1.permissions.add(pmod.Permission.objects.get(codename='can_search'))
    # g1.permissions.add(pmod.Permission.objects.get(codename='change_user'))

    # for p in pmod.Permission.objects.all():
    #     print(p)

    # p = pmod.Permission()
    # p.codename='view_analytics'
    # p.name='can view analytics'
    # p.content_type=pmod.Permission.objects.get(codename='add_user').content_type
    # p.save()
       

    # user = User.objects.create_user(first_name = 'Trent', last_name = 'McMillan', username='pro',
    #                              email='test@test.com',
    #                              password='pro')
    # user.groups.add(pmod.Group.objects.get(name='Pro'))

    # user.save()

    # user = User.objects.create_user(first_name = 'Amanda', last_name = 'McMillan', username='regular',
    #                              email='test@test.com',
    #                              password='regular')
    # user.groups.add(pmod.Group.objects.get(name='Regular'))

    # user.save()


    # product = stripe.Product.create(
    #     name='Dirt Bike Deals Subscription',
    #     type='service',
    # )
    
    # plan = stripe.Plan.create(
    #     nickname="Standard Monthly",
    #     product= product['id'],
    #     amount=2000,
    #     currency="usd",
    #     interval="month",
    #     usage_type="licensed",
    # )

    # subscription = hmod.Subscription()
    # subscription.product_id = product['id']
    # subscription.plan_id = plan['id']  
    # subscription.save()



    context = {

    }

    return request.dmp.render('index.html', context)

