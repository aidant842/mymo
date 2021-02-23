from django.shortcuts import render
from django.utils import timezone

from .models import Listing


def all_listings_view(request):
    """ A view to return all listings """

    listings = Listing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),)

    template = 'listings/all_listings.html'
    context = {
        'listings': listings,
    }

    return render(request, template, context)
