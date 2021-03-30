from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import UserProfile
from checkout.models import Order
from listings.models import SaleListing, RentListing

from operator import attrgetter
from itertools import chain


@login_required
def profile(request):
    """ Display User's Profile """

    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'profile': profile,
    }

    return render(request, template, context)


def public_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, pk=profile_id)
    sale_listings = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), user_profile=profile)
    rent_listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), user_profile=profile)

    result_list = list(chain(sale_listings, rent_listings))

    result_list.sort(key=attrgetter('date_created'), reverse=True)
    result_list.sort(key=attrgetter('is_spotlight'), reverse=True)

    orders = profile.orders.all()

    profile_orders = Order.objects.filter(user_profile=profile)
    profile_orders.order_by('-date')

    template = 'profiles/public_profile.html'

    context = {
        'profile': profile,
        'orders': orders,
        'result_list': result_list,
    }

    return render(request, template, context)