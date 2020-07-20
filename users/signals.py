from django.db.models.signals import post_save # creates signal
from django.contrib.auth.models import User  # sender
from django.dispatch import receiver # reciever
from .models import Profile

# When user is saved, send this signal
# signal will be recieved by create_profile function
# parameters passed by post_save will be passed
# on to create_profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
