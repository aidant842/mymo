from django.shortcuts import render
from django.utils import timezone

from listings.models import Listing


def index(request):
    """ A view to return the home """

    spotlight_listings = Listing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), is_spotlight=True)

    context = {
        'counter': 10,
        'spotlight_listings': spotlight_listings,
    }

    template = 'home/index.html'
    return render(request, template, context)
