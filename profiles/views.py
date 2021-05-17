from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import UserProfile
from .forms import UserProfileForm, AgentProfileForm
from checkout.models import Order
from listings.models import SaleListing, RentListing, SaleListingImage, RentListingImage
from products.models import Product
from analytics.models import ListingAnalytics

from operator import attrgetter
from itertools import chain


@login_required
def profile(request):
    """ Display User's Profile """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    profile_sale_listings = SaleListing.objects.filter(user_profile=profile)
    profile_rent_listings = RentListing.objects.filter(user_profile=profile)
    listing_analytics = ListingAnalytics.objects.get(pk=1)

    profile_listings = list(chain(profile_sale_listings, profile_rent_listings))
    profile_listings.sort(key=attrgetter('date_created'), reverse=True)

    if request.method == 'POST':
        if profile.is_agent:
            agent_profile_form = AgentProfileForm(request.POST, request.FILES, instance=profile)
            if agent_profile_form.is_valid():
                agent_profile_form.save()
                messages.success(request, 'Changes made successfully.')
                return redirect('profile')
            else:
                messages.error(request, 'Update failed, please ensure the form is valid.')
        else:
            user_profile_form = UserProfileForm(request.POST, instance=profile)

            if user_profile_form.is_valid():
                user_profile_form.save()
                messages.success(request, 'Changes made successfully.')
                return redirect('profile')
            else:
                messages.error(request,
                               'Update failed, please ensure the form is valid.')

    user_profile_form = UserProfileForm(instance=profile)
    agent_profile_form = AgentProfileForm(instance=profile)
    average_views = listing_analytics.average_listing_views
    users_sale_favourites = SaleListing.objects.filter(favourites=request.user, is_listed=True, expiration_date__gt=timezone.now())
    users_rent_favourites = RentListing.objects.filter(favourites=request.user, is_listed=True, expiration_date__gt=timezone.now())
    users_favourites = list(chain(users_sale_favourites, users_rent_favourites))

    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'profile': profile,
        'user_profile_form': user_profile_form,
        'agent_profile_form': agent_profile_form,
        'profile_listings': profile_listings,
        'average_views': average_views,
        'users_favourites': users_favourites,
    }

    return render(request, template, context)


@require_POST
@login_required
def delete_listing(request, listing_id):
    profile = UserProfile.objects.get(user=request.user)
    profile_sale_listings = SaleListing.objects.filter(user_profile=profile)
    profile_rent_listings = RentListing.objects.filter(user_profile=profile)

    profile_listings = list(chain(profile_sale_listings, profile_rent_listings))

    for listing in profile_listings:
        if listing.id == listing_id:
            listing.delete()

    messages.success(request, 'Your listing was successfully removed.')
    return redirect('profile')


@login_required
def favourite_sale_add(request, listing_id):
    try:
        listing = get_object_or_404(SaleListing, id=listing_id)
    except SaleListing.DoesNotExist:
        messages.error(request, 'Sorry an error has occured, object does not exist')
        return redirect('home')
    if listing.favourites.filter(id=request.user.id).exists():
        listing.favourites.remove(request.user)
        messages.success(request, 'Removed listing from your favourites.')
    else:
        listing.favourites.add(request.user)
        messages.success(request, 'Added listing to your favourites.')
    return redirect(reverse('sale_listing_detail', kwargs={'listing_id': listing.id}))


@login_required
def favourite_rent_add(request, listing_id):
    try:
        listing = get_object_or_404(RentListing, id=listing_id)
    except RentListing.DoesNotExist:
        messages.error(request, 'Sorry an error has occured, object does not exist')
        return redirect('home')
    if listing.favourites.filter(id=request.user.id).exists():
        listing.favourites.remove(request.user)
        messages.success(request, 'Removed listing from your favourites.')
    else:
        listing.favourites.add(request.user)
        messages.success(request, 'Added listing to your favourites.')
    return redirect(reverse('rent_listing_detail', kwargs={'listing_id': listing.id}))