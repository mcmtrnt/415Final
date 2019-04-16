from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


@view_function
def process_request(request):

    logout(request)

    context = {
        
    }
    return HttpResponseRedirect('/homepage/login/')