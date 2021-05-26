from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import PropertyRegsiterFilter
from listings.models import SoldListing, SaleListing, RentListing
from estate_agents.forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from itertools import chain
from operator import attrgetter


def property_register(request):
    filter_form = PropertyRegsiterFilter()

    listings = SoldListing.objects.all()

    if request.user.is_authenticated:
        contact_form = ContactForm(initial={'email': request.user.userprofile.email,
                                            'phone_number': request.user.userprofile.phone_number,
                                            'full_name': request.user.userprofile.full_name,})
    else:
        contact_form = ContactForm()

    query_dictionary = {}
    county_query = request.GET.get('county')
    area_query = request.GET.get('area')
    sort = request.GET.get('sort', None)

    if county_query != '' and county_query is not None:
        query_dictionary['county_query'] = county_query
        listings = listings.filter(county__icontains=county_query,)
    if area_query != '' and area_query is not None:
        query_dictionary['area_query'] = area_query
        area_queries = Q(area__icontains=area_query) | Q(county__icontains=area_query)
        listings = listings.filter(area_queries)
    if sort != '' and sort is not None:
        query_dictionary['sort'] = sort
        sortkey = sort.split('-')[0]
        direction = sort.split('-')[1]
        if direction == 'desc' or sortkey == 'date_created':
            sortkey = f'-{sortkey}'
        listings = listings.order_by(sortkey)
    else:
        listings = listings.order_by('-date_sold')

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

    template = 'price_register/property_register.html'
    context = {
        'filter_form': filter_form,
        'listings': listings,
        'query_dictionary': query_dictionary,
        'total_listings': total_listings,
        'page': page,
        'contact_form': contact_form,
    }

    return render(request, template, context)


def property_register_detail(request, listing_id):
    try:
        listing = get_object_or_404(SoldListing, pk=listing_id)
    except Exception as e:
        messages.error(request, f'{e}')
        return redirect(reverse('property_register'))

    if request.user.is_authenticated:
        contact_form = ContactForm(initial={'email': request.user.userprofile.email,
                                            'phone_number': request.user.userprofile.phone_number,
                                            'full_name': request.user.userprofile.full_name,})
    else:
        contact_form = ContactForm()
    profile = listing.user_profile.user.id
    show_recent_listings = False
    sale_listings = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), user_profile=profile)
    rent_listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), user_profile=profile)

    result_list = list(chain(sale_listings, rent_listings))

    for result in result_list:
        if result.id == listing.id:
            result_list.remove(result)

    if len(result_list) >= 1:
        show_recent_listings = True

    result_list.sort(key=attrgetter('date_created'), reverse=True)
    result_list = result_list[:3]

    template = 'price_register/property_register_detail.html'

    context = {
        'listing': listing,
        'contact_form': contact_form,
        'show_recent_listings': show_recent_listings,
        'result_list': result_list,
    }

    return render(request, template, context)