import imp
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

# LOG/AUTH


@receiver(user_logged_in, sender=User)
def logginSuccess(sender, request, user, **kwargs):
    print('-'*50)
    print('Logged In Successfully')

    print('Sender:', sender)
    print('Request:', request)
    print('User:', user)
    print(f'KWARGS: {kwargs}')

# user_logged_in.connect(logginSuccess, sender=User)


@receiver(user_logged_out, sender=User)
def logoutSuccess(sender, request, user, **kwargs):
    print('-'*50)
    print('Logged Out Successfully')
    print('Sender:', sender)
    print('Request:', request)
    print('User:', user)
    print(f'KWARGS: {kwargs}')

# user_logged_out.connect(logoutSuccess, sender=User)


@receiver(user_login_failed)
def loginFailed(sender, credentials, request, **kwargs):
    print('-'*50)
    print('Logged In Failed')
    print('Sender:', sender)
    print('credential:', credentials)
    print('Request:', request)
    print(f'KWARGS: {kwargs}')

# user_login_failed.connect(loginFailed)

# MODEL


@receiver(pre_save, sender=User)
def beforeSave(sender, instance, **kwargs):
    print('-'*50)
    print('Pre Save')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'KWARGS: {kwargs}')

# pre_save.connect(beforeSave,sender=User)


@receiver(post_save, sender=User)
def afterSave(sender, created, instance, **kwargs):
    print('-'*50)
    print('Post Save')
    print('Sender:', sender)
    print('Created:', created)
    print('Instance:', instance)
    print(f'KWARGS: {kwargs}')

# post_save.connect(afterSave,sender=User)


@receiver(pre_delete, sender=User)
def beforeDelete(sender, instance, **kwargs):
    print('-'*50)
    print('Pre Delete Signal')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'KWARGS: {kwargs}')

# pre_delete.connect(beforeDelete,sender=User)


@receiver(post_delete, sender=User)
def afterDelete(sender, instance, **kwargs):
    print('-'*50)
    print('Post Delete Signal')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'KWARGS: {kwargs}')

# post_delete.connect(afterDelete,sender=User)


@receiver(pre_init, sender=User)
def beforeInit(sender, *args, **kwargs):
    print('-'*50)
    print('Pre Initial Signal')
    print('Sender:', sender)
    print(f'Args: {args}')
    print(f'KWARGS: {kwargs}')


# pre_init.connect(beforeInit,sender=User)

@receiver(post_init, sender=User)
def afterInit(sender, *args, **kwargs):
    print('-'*50)
    print('Post Initial Signal')
    print('Sender:', sender)
    print(f'Args: {args}')
    print(f'KWARGS: {kwargs}')


# post_init.connect(afterInit,sender=User)

# Request/Response
@receiver(request_started)
def atBeginningRequest(sender, environ, **kwargs):
    print('-'*50)
    print('At Beginning of Request')
    print('Sender:', sender)
    print('Environ:', environ)
    print(f'KWARGS: {kwargs}')


@receiver(request_finished)
def atEndingRequest(sender, **kwargs):
    print('-'*50)
    print('At Ending of Request')
    print('Sender:', sender)
    print(f'KWARGS: {kwargs}')


@receiver(got_request_exception)
def atEndingRequest(sender, request, **kwargs):
    print('-'*50)
    print('At Ending of Request')
    print('Sender:', sender)
    print('Request:', request)

    print(f'KWARGS: {kwargs}')

# Management Signals/Migrate


@receiver(pre_migrate)
def beforeInstallApp(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('-'*50)
    print('Before Installing of App')
    print('Sender:', sender)
    print('App_Config:', app_config)
    print('verbosity:', verbosity)
    print('interactive:', interactive)
    print('using:', using)
    print('plan:', plan)
    print('apps:', apps)

    print(f'KWARGS: {kwargs}')


@receiver(post_migrate)
def atEndMigrateFlush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('-'*50)
    print('At End Migrate Flush')
    print('Sender:', sender)
    print('App_Config:', app_config)
    print('verbosity:', verbosity)
    print('interactive:', interactive)
    print('using:', using)
    print('plan:', plan)
    print('apps:', apps)

    print(f'KWARGS: {kwargs}')

# Databa e Wrapper


@receiver(connection_created)
def connDB(sender, connection, **kwargs):
    print('-'*50)
    print('Initail Connection to Database ')
    print('Sender:', sender)
    print('Connection:', connection)

    print(f'KWARGS: {kwargs}')
