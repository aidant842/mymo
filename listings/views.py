from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import SaleListing, RentListing, SaleListingImage, RentListingImage


def all_listings_view(request):
    """ A view to return all listings """

    for_sale_listings = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),)
    for_rent_listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),)

    template = 'listings/all_listings.html'
    context = {
        'for_sale_listings': for_sale_listings,
        'for_rent_listings': for_rent_listings,
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
