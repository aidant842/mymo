from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from listings.models import SaleListing, RentListing

from operator import attrgetter
from itertools import chain


@login_required
def profile(request):
    """ Display User's Profile """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST, instance=profile)

        if user_profile_form.is_valid():
            user_profile_form.save()
            messages.success(request, 'Changes made successfully.')
            return redirect('profile')
        else:
            messages.error(request,
                           'Update failed, please ensure the form is valid.')

    user_profile_form = UserProfileForm(instance=profile)


    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'profile': profile,
        'user_profile_form': user_profile_form,
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


@require_POST
@login_required
def delete_listing(request, order_id):
    order = Order.objects.get(pk=order_id)
    user_profile = UserProfile(user=request.user)

    if order.user_profile.user.id != user_profile.user.id:
        messages.success(request, 'You do not own this listing.')
        return redirect('home')

    if order.product.category.name == 'sale':
        listing_id = order.sale_listing.id
        listing = SaleListing(pk=listing_id)
        listing.delete()
    elif order.product.category.name == 'rent':
        listing_id = order.rent_listing.id
        listing = RentListing(pk=listing_id)
        listing.delete()
    messages.success(request, 'Your listing was successfully removed.')
    return redirect('profile')
