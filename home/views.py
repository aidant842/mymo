from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from operator import attrgetter

from listings.models import SaleListing, RentListing

from itertools import chain


def index(request):
    """ A view to return the home """

    all_sale_listings_count = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now()).count()
    all_rent_listings_count = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),).count()

    all_live_listings = all_sale_listings_count + all_rent_listings_count

    sale_spotlight_listings = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), is_spotlight=True)
    rent_spotlight_listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), is_spotlight=True)

    result_list = list(chain(sale_spotlight_listings, rent_spotlight_listings))

    result_list.sort(key=attrgetter('date_created'), reverse=True)

    context = {
        'sale_spotlight_listings': sale_spotlight_listings,
        'rent_spotlight_listings': rent_spotlight_listings,
        'result_list': result_list,
        'all_live_listings': all_live_listings,
    }

    template = 'home/index.html'
    return render(request, template, context)
