from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import *

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


