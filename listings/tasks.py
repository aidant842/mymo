from __future__ import absolute_import, unicode_literals
from django.utils import timezone
from celery import shared_task
from itertools import chain
import datetime

from celery.decorators import task

from .models import SaleListing, RentListing, SoldListing
from analytics.models import ListingAnalytics


@shared_task
def tasks():
    sale_listings = SaleListing.objects.all()
    rent_listings = RentListing.objects.all()

    listings = list(chain(sale_listings, rent_listings))

    for listing in listings:
        if not listing.sold:
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
        else:
            if listing.expiration_date < timezone.now():
                # If listing is sold and expired, archive it in soldListings and delete the origonal listing
                SoldListing.objects.create(
                    listing_number=listing.list_number,
                    user_profile=listing.user_profile,
                    county=listing.county,
                    area=listing.area,
                    eircode=listing.eircode,
                    property_type=listing.property_type,
                    price=listing.price_sold,
                    no_of_bedrooms=listing.no_of_bedrooms,
                    no_of_bathrooms=listing.no_of_bathrooms,
                    floor_area=listing.floor_area,
                    floor_area_type=listing.floor_area_type,
                    ber_rating=listing.ber_rating,
                    date_sold=listing.date_sold,
                )
                listing.delete()
                print(f'Completed creating new SoldListing objects, and deleted old SaleListing object {timezone.now()}')


@shared_task
def get_average_views():
    listing_analytics = ListingAnalytics.objects.get(pk=1)
    sale_listings = SaleListing.objects.all()
    rent_listings = RentListing.objects.all()
    viewed_total = 0

    listings = list(chain(sale_listings, rent_listings))

    for listing in listings:
        listing_views = listing.times_viewed
        viewed_total += listing_views

    average_views = int(viewed_total / len(listings))
    listing_analytics.average_listing_views = average_views
    listing_analytics.save()
    print(listing_analytics.average_listing_views)


