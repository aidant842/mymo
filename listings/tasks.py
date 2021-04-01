from __future__ import absolute_import, unicode_literals
from django.utils import timezone
from celery import shared_task
from itertools import chain
import datetime

from celery.decorators import task

from .models import SaleListing, RentListing


@shared_task
def tasks():
    sale_listings = SaleListing.objects.all()
    rent_listings = RentListing.objects.all()

    listings = list(chain(sale_listings, rent_listings))

    for listing in listings:
        # Delete an expired listing that wasn't renewed after 10 days from being unlisted
        if not listing.is_listed and listing.expiration_date < timezone.now():
            listing.delete()
            print(f'Completed deleting expired listings that were not renewed at {timezone.now()}')

        # Delete a listing that was created but not paid for after 24 hours from creation
        elif not listing.is_paid and listing.expiration_date < timezone.now():
            listing.delete()
            print(f'Completed delete if not paid after 24 hours of creation at {timezone.now()}')
        # Unlist listing that has expired, and set expiration for 10 days from being unlisted
        elif listing.expiration_date < timezone.now():
            listing.is_listed = False
            listing.expiration_date = timezone.now() + datetime.timedelta(days=10)
            listing.save()
            print(f'Completed unlisting at {timezone.now()}')
        # Remove premium status after 30 days
        elif listing.is_spotlight and listing.premium_expiration < timezone.now():
            listing.is_spotlight = False
            listing.save()
            print(f'Completed remove premium status at {timezone.now()}')

