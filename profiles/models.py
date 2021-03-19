from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """ A UserProfile Model """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=256, null=True, blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update the user profile """

    if created:
        UserProfile.objects.create(user=instance)
    # Existing Users: just save the profile
    instance.userprofile.save()
