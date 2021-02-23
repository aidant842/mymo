from __future__ import absolute_import, unicode_literals
from django.utils import timezone

from celery.decorators import task

from .models import Listing


@task(name='unlist_expired_listings')
def unlist_expired_listings():
    listings = Listing.objects.all()

    for listing in listings:
        if listing.expiration_date < timezone.now():
            listing.is_listed = False

    return f'Compelted unlisting at {timezone.now()}'
