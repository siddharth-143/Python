from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

# connecting the signals


@receiver(user_logged_in, sender=User)
# user login success
def login_success(sender, request, user, **kwargs):
    print("----------------------------------")
    print("Logged-in Signal... Run Intro..")
    print("Sender : ", sender)
    print("Request : ", request)
    print("User : ", user)
    print("User Password : ", user.password)
    print(f'kwargs : {kwargs}')
# connecting the signals
# user_logged_in.connect(login_success, sender=User)


# user logged out
@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print("----------------------------------")
    print("Logged-out Signal... Run Outro..")
    print("Sender : ", sender)
    print("Request : ", request)
    print("User : ", user)
    print("User Password : ", user.password)
    print(f'kwargs : {kwargs}')
# user_logged_out.connect(log_out, sender=User)


# user login failed
@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("----------------------------------")
    print("Logged Failed Signal...")
    print("Sender : ", sender)
    print("Credentails : ", credentials)
    print("Request : ", request)
    print(f'kwargs : {kwargs}')
# user_login_failed.connect(login_failed)

# pre_save


@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("----------------------------------")
    print("Pre Save Signal...")
    print("Sender : ", sender)
    print("Instances : ", instance)
    print(f'kwargs : {kwargs}')
# pre_save.connect(at_beginning_save, sender=User)


# post save
@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print("----------------------------------")
        print("Post Save Signal...")
        print("New Record")
        print("Sender : ", sender)
        print("Created : ", created)
        print("Instances : ", instance)
        print(f'kwargs : {kwargs}')
    else:
        print("----------------------------------")
        print("Post Save Signal...")
        print("Update")
        print("Sender : ", sender)
        print("Created : ", created)
        print("Instances : ", instance)
        print(f'kwargs : {kwargs}')
# post_save.connect(at_ending_save, sender=User)


# pre_delete
@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print("----------------------------------")
    print("Pre Delete Signal.......")
    print("Sender : ", sender)
    print("Instance : ", instance)
    print(f'kwargs : {kwargs}')
# pre_delete.connect(at_beginning_delete, snder=User)


# post delete
@receiver(post_delete, sender=User)
def at_endinging_delete(sender, instance, **kwargs):
    print("----------------------------------")
    print("Post Delete Signal.......")
    print("Sender : ", sender)
    print("Instance : ", instance)
    print(f'kwargs : {kwargs}')
# post_delete.connect(at_endinging_delete, snder=User)


# pre_init
@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("----------------------------------")
    print("Pre Init Signal.......")
    print("Sender : ", sender)
    print(f'Instance : {args}')
    print(f'kwargs : {kwargs}')
# pre_init.connect(at_beginning_init, snder=User)


# post_init
@receiver(post_init, sender=User)
def at_endinging_init(sender, instance, **kwargs):
    print("----------------------------------")
    print("Post Init Signal.......")
    print("Sender : ", sender)
    print("Instance : ", instance)
    print(f'kwargs : {kwargs}')
# post_init.connect(at_endinging_init, snder=User)


@receiver(request_started)
def at_beginning_requst(sender, environ, **kwargs):
    print("----------------------------------")
    print("At Beginning Request.......")
    print("Sender : ", sender)
    print("Environ : ", environ)
    print(f'kwargs : {kwargs}')
# request_started.connect(at_beginning_requst)


@receiver(request_finished)
def at_ending_requst(sender, **kwargs):
    print("----------------------------------")
    print("At Ending Request.......")
    print("Sender : ", sender)
    print(f'kwargs : {kwargs}')
# request_finished.connect(at_ending_requst)


@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print("----------------------------------")
    print("At Request Signal.......")
    print("Sender : ", sender)
    print("Request : ", request)
    print(f'kwargs : {kwargs}')
# got_request_exception.connect(at_req_exception)


@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("----------------------------------")
    print("Before_install_app.......")
    print("Sender : ", sender)
    print("App_config : ", app_config)
    print("verbosity : ", verbosity)
    print("interactive : ", interactive)
    print("Using : ", using)
    print("Plan : ", plan)
    print("Apps : ", apps)
    print(f'kwargs : {kwargs}')
# pre_migrate.connect(before_install_app)


@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("----------------------------------")
    print("at_end_migrate_flush.......")
    print("Sender : ", sender)
    print("App_config : ", app_config)
    print("verbosity : ", verbosity)
    print("interactive : ", interactive)
    print("Using : ", using)
    print("Plan : ", plan)
    print("Apps : ", apps)
    print(f'kwargs : {kwargs}')
# post_migrate.connect(at_end_migrate_flush)


@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print("----------------------------------")
    print("Sender : ", sender)
    print("Connection : ", connection)
    print(f'kwargs : {kwargs}')
# connection_created.connect(conn_db)7