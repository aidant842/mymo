from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.db.models import Q

from itertools import chain

from .models import SaleListing, RentListing, SaleListingImage, RentListingImage
from .forms import FilterForm


def all_listings_view(request):
    """ A view to return all listings """

    filters = FilterForm()
    for_sale_listings = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),)
    for_rent_listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),)
    result_list = list(chain(for_sale_listings, for_rent_listings))
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                """ Show message to user """
                return redirect(reverse('listings'))

            queries = Q(area__icontains=query) | Q(description__icontains=query) | Q(county__icontains=query) | Q(company_name__icontains=query)

            filtered_sale = for_sale_listings.filter(queries)
            filtered_rent = for_rent_listings.filter(queries)

            result_list = chain(filtered_sale, filtered_rent)

    template = 'listings/all_listings.html'
    context = {
        'filters': filters,
        'result_list': result_list,
        'search_term': query
    }

    return render(request, template, context)


def for_sale_listings(request):
    """ A view to return listings for sale """

    listings = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),)

    template = 'listings/for_sale.html'

    context = {
        'listings': listings,
    }

    return render(request, template, context)


def for_rent_listings(request):
    """ A view to return listings for sale """

    listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),)

    template = 'listings/for_rent.html'

    context = {
        'listings': listings,
    }

    return render(request, template, context)


def sale_listing_detail_view(request, listing_id):
    listing = get_object_or_404(SaleListing, pk=listing_id)
    photos = SaleListingImage.objects.filter(listing=listing)

    template = 'listings/for_sale_detail.html'

    context = {
        'listing': listing,
        'photos': photos,
    }

    return render(request, template, context)


def rent_listing_detail_view(request, listing_id):
    listing = get_object_or_404(RentListing, pk=listing_id)
    photos = RentListingImage.objects.filter(listing=listing)

    template = 'listings/for_rent_detail.html'

    context = {
        'listing': listing,
        'photos': photos,
    }

    return render(request, template, context)
