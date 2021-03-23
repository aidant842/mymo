from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from checkout.models import Order


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
    sale_listings = []
    rent_listings = []

    profile = get_object_or_404(UserProfile, pk=profile_id)

    orders = profile.orders.all()

    profile_orders = Order.objects.filter(user_profile=profile)

    for order in profile_orders:
        if order.product.category.name == 'sale':
            sale_listings.append(order.sale_listing)
        elif order.product.category.name == 'rent':
            rent_listings.append(order.rent_listing)

    template = 'profiles/public_profile.html'

    context = {
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)
