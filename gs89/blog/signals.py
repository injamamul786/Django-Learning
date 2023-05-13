from django.contrib.auth.signals import user_logged_in, user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_migrate, post_migrate, pre_init, pre_save, pre_delete,post_init,post_save, post_delete
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created
@receiver(user_logged_in, sender=User)
def loginSuccess(sender, request, user, **kwargs):
    print('-------')
    print('Logged-in Signal... Run Intro..')
    print('Sender:', sender)
    print('request', request)
    print('user', user)
    print('password:', user.password)
    print(f'kwargs: {kwargs}')

# user_logged_in.connect(loginSuccess, sender=User) #used when decorator not used


@receiver(user_logged_out, sender=User)
def logoutSuccess(sender, request, user, **kwargs):
    print('-------')
    print('Logged-out Signal... Run Outro..')
    print('Sender:', sender)
    print('request', request)
    print('user', user)
    print('password:', user.password)
    print(f'kwargs: {kwargs}')

#  user_logged_out.connect(logoutSuccess, sender=User) #used when decorator not used


@receiver(user_login_failed)
def loginFaild(sender,credentials, request,**kwargs):
    print('-------')
    print('Login Failed Signal...')
    print('Sender:', sender)
    print('credentials:', credentials)
    print('request', request)
    print(f'kwargs: {kwargs}')
# user_login_failed.connect(loginFaild)

@receiver(pre_save, sender=User)
def at_begining_save(sender, instance, **kwargs):
    print('-------------------')
    print('pre save Signal...')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'kwargs: {kwargs}')
# pre_save.connect(at_begining_save, sender=User)

@receiver(post_save, sender=User)
def at_ending_save(sender, instance,created, **kwargs):
    if created:
        print('-------------------')
        print('post save Signal...')
        print('new record')
        print('Sender:', sender)
        print('Instance:', instance)
        print('created:', created)
        print(f'kwargs: {kwargs}')
    else:
        print('-------------------')
        print('post save Signal...')
        print('update')
        print('Sender:', sender)
        print('Instance:', instance)
        print('created:', created)
        print(f'kwargs: {kwargs}')

# post_save.connect(at_ending_save, sender=User)

@receiver(pre_delete, sender=User)
def predelete(sender, instance, **kwargs):
    print('-------------------')
    print('pre delete Signal...')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'kwargs: {kwargs}')
# pre_delete.connect(predelete, sender=User)

@receiver(post_delete, sender=User)
def postdelete(sender, instance, **kwargs):
    print('-------------------')
    print('post delete Signal...')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'kwargs: {kwargs}')
# post_delete.connect(postdelete, sender=User)

@receiver(pre_init, sender=User)
def preinit(sender, *args, **kwargs):
    print('-------------------')
    print('pre init Signal...')
    print('Sender:', sender)
    print(f'Args: {args}')
    print(f'kwargs: {kwargs}')
# pre_init.connect(preinit, sender=User)

@receiver(post_init, sender=User)
def postinit(sender, *args, **kwargs):
    print('-------------------')
    print('post init Signal...')
    print('Sender:', sender)
    print(f'Args: {args}')
    print(f'kwargs: {kwargs}')

# post_init.connect(post_init, sender=User)

@receiver(request_started)
def at_begining_request(sender, environ, **kwargs):
    print('-------------------')
    print('At Bigning request Signal...')
    print('Sender:', sender)
    print('Environ:', environ)
    print(f'kwargs: {kwargs}')
# request_started.connect(at_begining_request)

@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print('-------------------')
    print('At ending request Signal...')
    print('Sender:', sender)        
    print(f'kwargs: {kwargs}')
request_finished.connect(at_ending_request)

@receiver(got_request_exception)
def at_req_exception(sender,request, **kwargs):
    print('----------------')
    print('at request exception.......')
    print('sender:', sender)
    print('request:', request)
    print(f'kwargs:{kwargs}')

# got_request_exception.connect(at_begining_request)



@receiver(pre_migrate)
def premigrate(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('--------------------------')
    print('pre migrate begore install app Signal....')
    print('Sender:', sender)
    print('app config:',app_config)
    print('verbosity:', verbosity)
    print('Interactive:', interactive)
    print('using:', using)
    print('plan:', plan)
    print('app:', apps)
    print(f'kwargs: {kwargs}')
# pre_migrate.connect(premigrate)

@receiver(post_migrate)
def postmigrate(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('--------------------------')
    print('post migrate after install app Signal....')
    print('Sender:', sender)
    print('app config:',app_config)
    print('verbosity:', verbosity)
    print('Interactive:', interactive)
    print('using:', using)
    print('plan:', plan)
    print('app:', apps)
    print(f'kwargs: {kwargs}')
# post_migrate.connect(postmigrate)

@receiver(connection_created)
def connectionsignal(sender, connection, **kwargs):
    print('-------------')
    print('Initial connection.....')
    print('sender:',sender)
    print('connaection:', connection)
    print(f'kwargs:{kwargs}')

# connection_created.connect(connectionsignal)