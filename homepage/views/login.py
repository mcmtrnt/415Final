from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core import validators
from django.core.exceptions import ValidationError

@view_function
def process_request(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('login'), password=form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponseRedirect('/homepage/deals/') #redirect to deals
    else:
        form = LoginForm()
    return request.dmp.render('login.html', {'form':form})

class LoginForm(forms.Form):
    login = forms.CharField(label='',  widget=forms.TextInput(attrs={'placeholder': 'username'}), max_length=100)
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    
    def clean(self):
        user = authenticate(username=self.cleaned_data.get('login'), password=self.cleaned_data.get('password'))
        if user is None:
            raise forms.ValidationError("Your username or password is incorrect")
        return self.cleaned_data