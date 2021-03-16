from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages

from listings.models import SaleListing, RentListing


def index(request):
    """ A view to return the home """

    messages.success(request, 'Welcome home')

    sale_spotlight_listings = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), is_spotlight=True)
    rent_spotlight_listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), is_spotlight=True)

    context = {
        'counter': 10,
        'sale_spotlight_listings': sale_spotlight_listings,
        'rent_spotlight_listings': rent_spotlight_listings,
    }

    template = 'home/index.html'
    return render(request, template, context)
