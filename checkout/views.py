import datetime
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.conf import settings

from products.models import Product
from products.forms import SaleListingForm, RentListingForm, SaleImageForm, RentImageForm
from listings.models import SaleListingImage, RentListingImage, SaleListing, RentListing
from checkout.forms import OrderForm

import stripe
import json


@require_POST
def cache_checkout_data(request):
    pid = request.POST.get('client_secret').split('_secret')[0]
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe.PaymentIntent.modify(pid, metadata = {

    })


@require_POST
def create_listings(request):
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        images = request.FILES.getlist('images')
        if product.category.name == 'sale':
            listing_form = SaleListingForm(request.POST, request.FILES)
            images_form = SaleImageForm(request.POST, request.FILES)
            if listing_form.is_valid() and images_form.is_valid():
                listing = listing_form.save(commit=False)
                listing.expiration_date = (timezone.now()
                                           + datetime.timedelta(days=365))
                if product.is_premium:
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
                return redirect('checkout')
        elif product.category.name == 'rent':
            listing_form = RentListingForm(request.POST, request.FILES)
            images_form = RentImageForm(request.POST, request.FILES)
            if listing_form.is_valid() and images_form.is_valid():
                listing = listing_form.save(commit=False)
                listing.expiration_date = (timezone.now()
                                           + datetime.timedelta(days=90))
                if product.is_premium:
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
                return redirect('checkout')
            else:
                for error in listing_form.errors:
                    print('listing form error ***********')
                    print(error)
                for error in images_form.errors:
                    print('images form error ***********')
                    print(error)


def checkout(request):

    listing_id = request.session.get('listing_id', '')
    product_id = request.session.get('product_id', '')
    product = get_object_or_404(Product, pk=product_id)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    order_form = OrderForm()

    if request.method == 'POST':
        if product.category.name == 'sale':
            listing = get_object_or_404(SaleListing, pk=listing_id)
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                listing.is_paid = True
                listing.save()
                order = order_form.save(commit=False)
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
                listing.save()
                order = order_form.save(commit=False)
                order.order_total = listing.product.price
                order.rent_listing = listing
                order.product = listing.product
                order.save()

                return redirect(reverse('checkout_success', args=[order.order_number]))

    if not product_id:
        print('returning to home no product_id')
        print(product_id)
        return redirect('home')

    if product.category.name == 'sale':
        listing = get_object_or_404(SaleListing, pk=listing_id)
    elif product.category.name == 'rent':
        listing = get_object_or_404(RentListing, pk=listing_id)
    stripe_total = product.price
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)

    if not stripe_public_key:
        print('********* ALERT STRIPE PUBLIC KEY NOT SET IN ENVIRON *************')

    template = 'checkout/checkout.html'
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'order_form': order_form,
        'product': product,
        'listing': listing,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    del request.session['listing_id']
    del request.session['product_id']
    template = 'checkout/checkout_success.html'
    return render(request, template)
