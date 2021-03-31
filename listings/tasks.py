from __future__ import absolute_import, unicode_literals
from django.utils import timezone
from celery import shared_task

from celery.decorators import task

from .models import SaleListing


@shared_task
def unlist_expired_listings():
    listings = SaleListing.objects.all()

    for listing in listings:
        if listing.expiration_date < timezone.now():
            listing.is_listed = False
            listing.save()

    return f'Compelted unlisting at {timezone.now()}'


@shared_task
def delete_listings():
    listings = SaleListing.objects.all()

    for listing in listings:
        listing.delete()


@shared_task
def say_hi():
    print('Hello from celery')
