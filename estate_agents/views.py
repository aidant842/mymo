from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils import timezone
from django.contrib import messages
from django.http import Http404
from listings.models import SaleListing, RentListing, SaleListingImage, RentListingImage
from profiles.models import UserProfile

from operator import attrgetter
from itertools import chain


def estate_agents(request):
    return redirect('home')


def estate_agents_profile(request, name, profile_id):
    profile = get_object_or_404(UserProfile, pk=profile_id)
    print(type(name))
    print(type(profile.company_name_to_url()))
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

    template = 'estate_agents/estate_agents_profile.html'

    context = {
        'profile': profile,
        'result_list': result_list,
    }

    return render(request, template, context)
