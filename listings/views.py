from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from itertools import chain
from operator import attrgetter

from .models import SaleListing, RentListing, SaleListingImage, RentListingImage
from .forms import FilterForm


def all_listings_view(request):
    """ A view to return all listings """

    """ IF ADDING FILTERS TO THIS VIEW """
    """ FILTER FORSALE AND FORRENT FIRST, THEN CHAIN INTO LIST """

    filter_form = FilterForm()
    for_sale_listings = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),)
    for_rent_listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),)
    result_list = list(chain(for_sale_listings, for_rent_listings))
    result_list.sort(key=attrgetter('date_created'), reverse=True)
    result_list.sort(key=attrgetter('is_spotlight'), reverse=True)
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

    """ setup paginator """

    paginator = Paginator(result_list, 20)
    page = request.GET.get('page')

    try:
        result_list = paginator.page(page)
    except PageNotAnInteger:
        result_list = paginator.page(1)

    except EmptyPage:
        result_list = paginator.page(paginator.num_pages)

    total_listings = len(result_list)

    template = 'listings/all_listings.html'
    context = {
        'filter_form': filter_form,
        'result_list': result_list,
        'search_term': query,
        'total_listings': total_listings,
        'query': query,
    }

    return render(request, template, context)


def for_sale_listings(request):
    """ A view to return listings for sale """

    filter_form = FilterForm()

    listings = SaleListing.objects.filter(is_listed=True,
                                          expiration_date__gt=timezone.now(),)

    query_dictionary = {}
    price_query = request.GET.get('price')
    county_query = request.GET.get('county')
    property_type_query = request.GET.get('property_type')
    no_of_bedrooms_query = request.GET.get('bedrooms')
    no_of_bathrooms_query = request.GET.get('bathrooms')
    ber_rating_query = request.GET.get('ber_rating')
    custom_query = request.GET.get('query')
    sort = request.GET.get('sort', None)

    if price_query != '' and price_query is not None:
        query_dictionary['price_query'] = price_query
        price_query = int(price_query)
        listings = listings.filter(price__lte=price_query,)
    if county_query != '' and county_query is not None:
        query_dictionary['county_query'] = county_query
        listings = listings.filter(county__icontains=county_query,)
    if property_type_query != '' and property_type_query is not None:
        query_dictionary['property_type_query'] = property_type_query
        listings = listings.filter(property_type__icontains=property_type_query,)
    if no_of_bedrooms_query != '' and no_of_bathrooms_query is not None:
        query_dictionary['no_of_bedrooms_query'] = no_of_bedrooms_query
        listings = listings.filter(no_of_bedrooms__gte=no_of_bedrooms_query,)
    if no_of_bathrooms_query != '' and no_of_bathrooms_query is not None:
        query_dictionary['no_of_bathrooms_query'] = no_of_bathrooms_query
        listings = listings.filter(no_of_bathrooms__gte=no_of_bathrooms_query,)
    if ber_rating_query != '' and ber_rating_query is not None:
        query_dictionary['ber_rating_query'] = ber_rating_query
        listings = listings.filter(ber_rating__icontains=ber_rating_query,)
    if custom_query != '' and custom_query is not None:
        query_dictionary['custom_query'] = custom_query
        queries = Q(area__icontains=custom_query) | Q(description__icontains=custom_query) | Q(county__icontains=custom_query) | Q(company_name__icontains=custom_query) 
        listings = listings.filter(queries)
    if sort != '' and sort is not None:
        query_dictionary['sort'] = sort
        sortkey = sort.split('-')[0]
        direction = sort.split('-')[1]
        if direction == 'desc' or sortkey == 'date_created':
            sortkey = f'-{sortkey}'
        listings = listings.order_by(sortkey)
    else:
        listings = listings.order_by('-is_spotlight', '-date_created')

    total_listings = listings.count()

    """ setup paginator """

    paginator = Paginator(listings, 20)
    page = request.GET.get('page')

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)

    except EmptyPage:
        listings = paginator.page(paginator.num_pages)

    template = 'listings/for_sale.html'

    context = {
        'filter_form': filter_form,
        'listings': listings,
        'query_dictionary': query_dictionary,
        'total_listings': total_listings,
        'page': page,
    }

    return render(request, template, context)


def for_rent_listings(request):
    """ A view to return listings for sale """
    filter_form = FilterForm()
    listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(),)

    query_dictionary = {}
    price_query = request.GET.get('price')
    county_query = request.GET.get('county')
    property_type_query = request.GET.get('property_type')
    no_of_bedrooms_query = request.GET.get('bedrooms')
    no_of_bathrooms_query = request.GET.get('bathrooms')
    ber_rating_query = request.GET.get('ber_rating')
    custom_query = request.GET.get('query')
    sort = request.GET.get('sort')

    if price_query != '' and price_query is not None:
        query_dictionary['price_query'] = price_query
        price_query = int(price_query)
        listings = listings.filter(price__lte=price_query,)
    if county_query != '' and county_query is not None:
        query_dictionary['county_query'] = county_query
        listings = listings.filter(county__icontains=county_query,)
    if property_type_query != '' and property_type_query is not None:
        query_dictionary['property_type_query'] = property_type_query
        listings = listings.filter(property_type__icontains=property_type_query,)
    if no_of_bedrooms_query != '' and no_of_bathrooms_query is not None:
        query_dictionary['no_of_bedrooms_query'] = no_of_bedrooms_query
        listings = listings.filter(no_of_bedrooms__gte=no_of_bedrooms_query,)
    if no_of_bathrooms_query != '' and no_of_bathrooms_query is not None:
        query_dictionary['no_of_bathrooms_query'] = no_of_bathrooms_query
        listings = listings.filter(no_of_bathrooms__gte=no_of_bathrooms_query,)
    if ber_rating_query != '' and ber_rating_query is not None:
        query_dictionary['ber_rating_query'] = ber_rating_query
        listings = listings.filter(ber_rating__icontains=ber_rating_query,)
    if custom_query != '' and custom_query is not None:
        query_dictionary['custom_query'] = custom_query
        queries = Q(area__icontains=custom_query) | Q(description__icontains=custom_query) | Q(county__icontains=custom_query) | Q(company_name__icontains=custom_query) 
        listings = listings.filter(queries)
    if sort != '' and sort is not None:
        query_dictionary['sort'] = sort
        sortkey = sort.split('-')[0]
        direction = sort.split('-')[1]
        if direction == 'desc' or sortkey == 'date_created':
            sortkey = f'-{sortkey}'
        listings = listings.order_by(sortkey)
    else:
        listings = listings.order_by('-is_spotlight', '-date_created')

    total_listings = listings.count()

    """ setup paginator """

    paginator = Paginator(listings, 20)
    page = request.GET.get('page')

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(paginator.num_pages)

    template = 'listings/for_rent.html'

    context = {
        'filter_form': filter_form,
        'listings': listings,
        'total_listings': total_listings,
        'page': page,
    }

    return render(request, template, context)


def sale_listing_detail_view(request, listing_id):
    listing = get_object_or_404(SaleListing, pk=listing_id)
    if listing.times_viewed is None:
        listing.times_viewed = 1
        listing.save()
    else:
        listing.times_viewed += 1
        listing.save()

    photos = list(SaleListingImage.objects.filter(listing=listing))
    photos.insert(0, listing.header_image.url)
    no_of_photos = len(photos)

    template = 'listings/for_sale_detail.html'

    context = {
        'listing': listing,
        'photos': photos,
        'no_of_photos': no_of_photos,
    }

    if listing.is_listed:
        return render(request, template, context)
    else:
        messages.error(request, 'Listing does not exist or has expired')
        return redirect(reverse('home'))


def rent_listing_detail_view(request, listing_id):
    listing = get_object_or_404(RentListing, pk=listing_id)
    if listing.times_viewed is None:
        listing.times_viewed = 1
        listing.save()
    else:
        listing.times_viewed += 1
        listing.save()

    photos = list(RentListingImage.objects.filter(listing=listing))
    photos.insert(0, listing.header_image.url)
    no_of_photos = len(photos)

    template = 'listings/for_rent_detail.html'

    context = {
        'no_of_photos': no_of_photos,
        'listing': listing,
        'photos': photos,
    }
    if listing.is_listed:
        return render(request, template, context)
    else:
        messages.error(request, 'Listing does not exist or has expired')
        return redirect(reverse('home'))
