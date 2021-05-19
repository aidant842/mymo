from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """ A UserProfile Model """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=256, null=True, blank=True)
    company_logo = models.ImageField(upload_to='agent_logos', null=True, blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    psr_number = models.CharField(max_length=256, null=True, blank=True)
    is_agent = models.BooleanField(default=False)
    subscription_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def company_name_to_url(self):
        if self.company_name:
            return self.company_name.replace(' ', '-')
        else:
            return str(self.user)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update the user profile """

    if created:
        UserProfile.objects.create(user=instance, email=instance.email)
    # Existing Users: just save the profile
    instance.userprofile.save()
