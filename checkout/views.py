import datetime
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.conf import settings

from products.models import Product
from products.forms import SaleListingForm, RentListingForm, SaleImageForm, RentImageForm
from listings.models import SaleListingImage, RentListingImage, SaleListing, RentListing
from checkout.forms import OrderForm
from profiles.models import UserProfile
from coupons.models import Coupon
from coupons.forms import CouponApplyForm

from .models import Order

import stripe
import json


@require_POST
def apply_coupon(request):
    try:
        coupon_code = request.POST.get('coupon_code')
        return
    except Exception as e:
        messages.error(request, 'An error occured when applying that coupon code')
        return HttpResponse(content=e, status=400)

@require_POST
def cache_checkout_data(request):
    try:
        listing_id = request.session.get('listing_id', '')
        product_id = request.session.get('product_id', '')
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata = {
            'listing_id': listing_id,
            'product_id': product_id,
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry your payment cannot be \
            processed right now. Please try again later')
        return HttpResponse(content=e, status=400)


@login_required
@require_POST
def create_listings(request):
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)

    if request.session.get('listing_id'):
        return redirect('checkout')
    else:
        if request.method == 'POST':
            images = request.FILES.getlist('images')
            if product.category.name == 'sale':
                listing_form = SaleListingForm(request.POST, request.FILES)
                images_form = SaleImageForm(request.POST, request.FILES)
                if listing_form.is_valid() and images_form.is_valid():
                    listing = listing_form.save(commit=False)
                    listing.expiration_date = (timezone.now()
                                            + datetime.timedelta(days=1))
                    if product.is_premium:
                        listing.is_spotlight = True
                        listing.premium_expiration = (timezone.now()
                                                    + datetime.timedelta(days=30))
                    listing.product = product
                    listing.save()
                    request.session['listing_id'] = listing.id
                    request.session['product_id'] = product_id
                    for image in images:
                        SaleListingImage.objects.create(
                            listing=listing,
                            images=image
                        )
                    if user.is_agent and user.subscription_paid and not product.is_premium:
                        listing.is_paid = True
                        listing.user_profile = user
                        listing.save()
                        messages.success(request, 'Your listing has been submitted, please allow upto 48 hours for it to be reviewed by one of our team')
                        return redirect('home')
                    else:
                        return redirect('checkout')
                else:
                    messages.error(request, 'form error, try re-uploading images')
                    return redirect(reverse('product_detail', kwargs={'product_id':product.id}))
            elif product.category.name == 'rent':
                listing_form = RentListingForm(request.POST, request.FILES)
                images_form = RentImageForm(request.POST, request.FILES)
                if listing_form.is_valid() and images_form.is_valid():
                    listing = listing_form.save(commit=False)
                    listing.expiration_date = (timezone.now()
                                            + datetime.timedelta(days=1))
                    if product.is_premium:
                        listing.is_spotlight = True
                        listing.premium_expiration = (timezone.now()
                                                    + datetime.timedelta(days=30))
                    listing.product = product
                    listing.save()
                    request.session['listing_id'] = listing.id
                    request.session['product_id'] = product_id
                    for image in images:
                        RentListingImage.objects.create(
                            listing=listing,
                            images=image
                        )
                    if user.is_agent and user.subscription_paid  and not product.is_premium:
                        listing.is_paid = True
                        listing.user_profile = user
                        listing.save()
                        messages.success(request, 'Your listing has been submitted, please allow upto 48 hours for it to be reviewed by one of our team')
                        return redirect('home')
                    else:
                        return redirect('checkout')
                else:
                    for error in listing_form.errors:
                        print('listing form error ***********')
                        print(error)
                    for error in images_form.errors:
                        print('images form error ***********')
                        print(error)
                    messages.error(request, 'form error, try re-uploading images')
                    return redirect(reverse('product_detail', kwargs={'product_id':product.id}))


@login_required
def checkout(request):

    listing_id = request.session.get('listing_id', '')
    if not listing_id or listing_id == '':
        messages.error(request, 'There was an error processing your request, \
            if this continues please contact us.')
        return redirect('home')
    product_id = request.session.get('product_id', '')
    product = get_object_or_404(Product, pk=product_id)
    profile = UserProfile.objects.get(user=request.user)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    order_form = OrderForm()
    coupon_form = CouponApplyForm()

    if request.method == 'POST':
        if product.category.name == 'sale':
            listing = get_object_or_404(SaleListing, pk=listing_id)
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                listing.is_paid = True
                listing.user_profile = profile
                listing.expiration_date = (timezone.now()
                                           + datetime.timedelta(days=365))
                listing.save()
                order = order_form.save(commit=False)
                pid = request.POST.get('client_secret').split('_secret')[0]
                order.stripe_pid = pid
                order.order_total = listing.product.price
                order.sale_listing = listing
                order.product = listing.product
                order.save()

                return redirect(reverse('checkout_success', args=[order.order_number]))
        elif product.category.name == 'rent':
            listing = get_object_or_404(RentListing, pk=listing_id)
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                listing.is_paid = True
                listing.user_profile = profile
                listing.expiration_date = (timezone.now()
                                           + datetime.timedelta(days=90))
                listing.save()
                order = order_form.save(commit=False)
                pid = request.POST.get('client_secret').split('_secret')[0]
                order.stripe_pid = pid
                order.order_total = listing.product.price
                order.rent_listing = listing
                order.product = listing.product
                order.save()

                return redirect(reverse('checkout_success', args=[order.order_number]))

    if not product_id:
        return redirect('home')

    if product.category.name == 'sale':
        listing = get_object_or_404(SaleListing, pk=listing_id)
    elif product.category.name == 'rent':
        listing = get_object_or_404(RentListing, pk=listing_id)

    coupon_id = request.session.get('coupon_id')
    if coupon_id is not None:
        coupon = Coupon.objects.get(pk=coupon_id)
        discount = (coupon.discount / Decimal('100') * product.price)
        stripe_total = int(product.price - discount)
    else:
        stripe_total = product.price

    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.error(request, '********* ALERT STRIPE PUBLIC KEY NOT SET IN ENVIRON *************')

    template = 'checkout/checkout.html'
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'order_form': order_form,
        'coupon_form': coupon_form,
        'product': product,
        'listing': listing,
        'stripe_total': stripe_total,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()
    if not request.session.get('listing_id'):
        messages.error(request, 'There was an error processing your request, \
            if this continues please contact us.')
        return redirect('home')
    del request.session['listing_id']
    del request.session['product_id']
    if 'coupon_id' in request.session:
        del request.session['coupon_id']
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
