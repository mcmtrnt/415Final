# from django.conf import settings
# from django_mako_plus import view_function, jscontext
# from django import forms
# from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
# from django.contrib.auth import models as pmod
# from homepage import models as hmod
# # import stripe


# @view_function
# def process_request(request):

#     if request.method == 'POST':  #when stripe comes back this will be true. 
#         form = CheckoutForm(request.POST)
#         form.user_id = request.user.id
#         if form.is_valid():

#             try:
#                 charge = stripe.Charge.create(
#                     amount= 1000, 
#                     currency='usd',
#                     description='Charge for pro account',
#                     source=form.cleaned_data.get('stripeToken'),
#                 )

#                 user = User.objects.get(id = request.user.id)
#                 user.groups.add(pmod.Group.objects.get(name='Pro')) #add user to the pro group

#                 user.save()

#                 pro = hmod.Pros()
#                 pro.user_id = user.id
#                 pro.charge_id = charge['id']  #record the sale
#                 pro.save()


#             except Exception as e:
#                 raise forms.ValidationError('Error processing payment: {}'.format(e))

#             return HttpResponseRedirect('/homepage/receipt/') 
            
#     else:
#         form = CheckoutForm()

#     context = {
#         'form': form,
#     }
#     return request.dmp.render('/homepage/templates/checkout.html', context)


# class CheckoutForm(forms.Form):
#     address = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'address'}), max_length=100)
#     city = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'city'}), max_length=100)
#     state = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'state'}), max_length=100)
#     zipcode = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'zipcode'}), max_length=100)
#     stripeToken = forms.CharField(widget=forms.HiddenInput())

#     def clean(self):

#         pros = hmod.Pros.objects.filter(user_id = self.user_id)
#         if len(pros) > 0:
#             raise forms.ValidationError("You have already purchased the pro account")
#             #raise ValueError('You have already purchased the pro account')

#         return self.cleaned_data