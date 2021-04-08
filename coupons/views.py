from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm


@require_POST
def apply_coupon(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['coupon_id'] = coupon.id
            messages.success(request, 'Coupon code applied.')
        except Coupon.DoesNotExist:
            messages.error(request, 'Coupon has either expired or doesn\'t exist')
            request.session['coupon_id'] = None
    return redirect('checkout')

