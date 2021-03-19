from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from checkout.models import Order


@login_required
def profile(request):
    """ Display User's Profile """

    sale_listings = []
    rent_listings = []

    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    profile_orders = Order.objects.filter(user_profile=request.user.userprofile)

    for order in profile_orders:
        if order.product.category.name == 'sale':
            sale_listings.append(order.sale_listing)
        elif order.product.category.name == 'rent':
            rent_listings.append(order.rent_listing)


    """ sale_listings = profile.orders.sale_listing
    rent_listings = profile.orders.rent_listing """

    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'profile': profile,
        'profile_orders': profile_orders,
        'sale_listings': sale_listings,
        'rent_listings': rent_listings,
    }

    return render(request, template, context)
