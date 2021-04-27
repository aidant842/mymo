from django.shortcuts import render
from django.utils import timezone
from operator import attrgetter

from listings.models import SaleListing, RentListing

from itertools import chain

import os


def index(request):
    """ A view to return the home """

    request.session['dev'] = 'DEVELOPMENT' in os.environ

    all_sale_listings_count = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now()).count()
    all_rent_listings_count = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),).count()

    all_live_listings = all_sale_listings_count + all_rent_listings_count

    sale_spotlight_listings = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), is_spotlight=True)
    rent_spotlight_listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), is_spotlight=True)

    result_list = list(chain(sale_spotlight_listings, rent_spotlight_listings))

    result_list.sort(key=attrgetter('date_created'), reverse=True)
    result_list = result_list[:8]

    context = {
        'sale_spotlight_listings': sale_spotlight_listings,
        'rent_spotlight_listings': rent_spotlight_listings,
        'result_list': result_list,
        'all_live_listings': all_live_listings,
    }

    template = 'home/index.html'
    return render(request, template, context)


def error_404_view(request, exception):
    """ A view to return custom 404 page """

    template = 'home/404.html'

    return render(request, template, status=404)


def error_500_view(request):
    """ A view to return custom 500 page """

    template = 'home/500.html'

    return render(request, template, status=500)
