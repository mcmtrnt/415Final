from django.conf import settings
from django_mako_plus import view_function, jscontext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import models as pmod
from homepage import models as hmod
import stripe


@view_function
def process_request(request):

    pro = hmod.Pros.objects.get(user_id = request.user.id)
    sub = stripe.Subscription.retrieve(pro.subscription_id)
    stripe.Subscription.delete(stripe.Subscription.retrieve(sub.id))

    user = User.objects.get(id = request.user.id)
    user.groups.remove(pmod.Group.objects.get(name='Pro'))
    user.save()

    pro.delete()

    context = {
    }
    return request.dmp.render('/homepage/templates/cancel.html', context)