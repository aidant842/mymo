from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.db.models import Q

from itertools import chain
import operator

from .models import SaleListing, RentListing, SaleListingImage, RentListingImage
from .forms import FilterForm


def all_listings_view(request):
    """ A view to return all listings """

    filter_form = FilterForm()
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

            result_list = list(chain(filtered_sale, filtered_rent))

    template = 'listings/all_listings.html'
    context = {
        'filter_form': filter_form,
        'result_list': result_list,
        'search_term': query
    }

    return render(request, template, context)


def for_sale_listings(request):
    """ A view to return listings for sale """


    filter_form = FilterForm()

    listings = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),)

    if request.method == 'POST':
        price = request.POST.get('price')
        county = request.POST.get('county')
        property_type = request.POST.get('property_type')
        no_of_bedrooms = request.POST.get('bedrooms')
        no_of_bathrooms = request.POST.get('bathrooms')
        ber_rating = request.POST.get('ber_rating')
        category = request.POST.get('category')
        listings = SaleListing.objects.filter(
                                        is_listed=True,
                                        expiration_date__gt=timezone.now(),)
        if price != '':
            listings = listings.filter(price__lte=price)
        if county != '':
            listings = listings.filter(county=county)
        if property_type != '':
            listings = listings.filter(property_type=property_type)
        if no_of_bedrooms != '':
            listings = listings.filter(no_of_bedrooms=no_of_bedrooms)
        if no_of_bathrooms != '':
            listings = listings.filter(no_of_bathrooms=no_of_bathrooms)
        if ber_rating != '':
            listings = listings.filter(ber_rating=ber_rating)
        if category != '':
            listings = listings.filter(category__name__in=category)

    template = 'listings/for_sale.html'

    context = {
        'filter_form': filter_form,
        'listings': listings,
    }

    return render(request, template, context)


def for_rent_listings(request):
    """ A view to return listings for sale """
    filter_form = FilterForm()
    listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),)

    template = 'listings/for_rent.html'

    context = {
        'filter_form': filter_form,
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
