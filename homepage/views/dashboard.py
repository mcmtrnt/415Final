from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django.db.models import Avg
import requests

@view_function
def process_request(request):
    

    context = {

    }

    return request.dmp.render('dashboard.html', context)