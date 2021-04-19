from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils import timezone
from django.contrib import messages
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.models import SaleListing, RentListing, SaleListingImage, RentListingImage
from profiles.models import UserProfile

from operator import attrgetter
from itertools import chain


def estate_agents(request):
    return redirect('home')


def estate_agents_profile(request, name, profile_id):
    profile = get_object_or_404(UserProfile, pk=profile_id)
    if not name == profile.company_name_to_url():
        raise Http404
    if not profile.is_agent:
        messages.error(request, 'This user is not an agent.')
        return redirect('home')
    sale_listings = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), user_profile=profile)
    rent_listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), user_profile=profile)

    result_list = list(chain(sale_listings, rent_listings))

    result_list.sort(key=attrgetter('date_created'), reverse=True)
    result_list.sort(key=attrgetter('is_spotlight'), reverse=True)
    total_listings = len(result_list)

    """ setup paginator """

    paginator = Paginator(result_list, 20)
    page = request.GET.get('page')

    try:
        result_list = paginator.page(page)
    except PageNotAnInteger:
        result_list = paginator.page(1)

    except EmptyPage:
        result_list = paginator.page(paginator.num_pages)

    template = 'estate_agents/estate_agents_profile.html'

    context = {
        'profile': profile,
        'result_list': result_list,
        'total_listings': total_listings,
    }

    return render(request, template, context)
