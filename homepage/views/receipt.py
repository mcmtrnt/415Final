from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms
from django.http import HttpResponseRedirect

@view_function
def process_request(request):

    return request.dmp.render('receipt.html')