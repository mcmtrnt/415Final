from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import models as pmod

@view_function
def process_request(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            user = User.objects.create_user(first_name = form.cleaned_data.get('Fname'),
                last_name = form.cleaned_data.get('Lname'), 
                email=form.cleaned_data.get('email'),
                username=form.cleaned_data.get('username'),     
                password=form.cleaned_data.get('password'))

            # a regular group is not necessary
            #user.groups.add(pmod.Group.objects.get(name='Regular'))    #add the user to the basic group

            user.save()

            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)

            return HttpResponseRedirect('/homepage/success/') #redirect to success page
    else:
        form = LoginForm()
    return request.dmp.render('signup.html', {'form':form})

class LoginForm(forms.Form):
    Fname = forms.CharField(label='',  widget=forms.TextInput(attrs={'placeholder': 'first name'}), max_length=100)
    Lname = forms.CharField(label='',  widget=forms.TextInput(attrs={'placeholder': 'last name'}), max_length=100)
    email = forms.CharField(label='',  widget=forms.TextInput(attrs={'placeholder': 'email'}), max_length=100)
    username = forms.CharField(label='',  widget=forms.TextInput(attrs={'placeholder': 'username'}), max_length=100)
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    
    def clean(self):
        user = pmod.User.objects.filter(username = self.cleaned_data.get('username'))
        if len(user) > 0:
            raise forms.ValidationError("That username is already taken")
        return self.cleaned_data