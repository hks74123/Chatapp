from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from . import views
from django.db.models.signals import post_save
from .models import Chat

@receiver(user_logged_in, sender=User)
def new_device_login(sender, user, request, **kwargs):
    user_mail = user.email
    res = views.new_device_mail(user_mail)

@receiver(post_save, sender=Chat)
def add_notification(sender, instance, **kwargs):
    print('New Chat -------------------')
    print(kwargs)

