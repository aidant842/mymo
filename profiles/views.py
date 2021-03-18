from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile


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
