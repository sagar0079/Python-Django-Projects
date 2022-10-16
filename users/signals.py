# type: ignore
from django import dispatch
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from . models import Profile

@receiver(post_save,sender=User,dispatch_uid = 'user.build_profile')
def build_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User,dispatch_uid = 'user.save_profile')
def save_profile(sender,instance,**kwargs):
    instance.profile.save()