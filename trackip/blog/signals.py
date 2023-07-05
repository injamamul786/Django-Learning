from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    # print('-------------------')
    # print('logged in signal.. run intro')
    ipadd = request.META.get('REMOTE_ADDR')
    # print('ip address:', ipadd)
    request.session['ip'] = ipadd