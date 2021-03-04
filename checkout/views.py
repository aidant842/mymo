import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from products.models import Product
from products.forms import SaleListingForm, RentListingForm, SaleImageForm, RentImageForm
from listings.models import SaleListingImage, RentListingImage
from checkout.forms import OrderForm
from checkout.models import Order


def checkout(request):
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        images = request.FILES.getlist('images')
        if product.category.name == 'sale':
            listing_form = SaleListingForm(request.POST, request.FILES)
            images_form = SaleImageForm(request.POST, request.FILES)
            order_form = OrderForm(request.POST)
            if listing_form.is_valid() and images_form.is_valid() and order_form.is_valid():
                listing = listing_form.save(commit=False)
                listing.expiration_date = (timezone.now()
                                           + datetime.timedelta(days=365))
                if product.is_premium:
                    listing.premium_expiration = (timezone.now()
                                                  + datetime.timedelta(days=30))
                listing.product = product
                listing.save()
                for image in images:
                    SaleListingImage.objects.create(
                        listing=listing,
                        images=image
                    )
                order = order_form.save(commit=False)
                order.order_total = product.price
                order.sale_listing = listing
                order.product = product
                order.save()
                return redirect('home')
        elif product.category.name == 'rent':
            listing_form = RentListingForm(request.POST, request.FILES)
            images_form = RentImageForm(request.POST, request.FILES)
            order_form = OrderForm(request.POST)
            if listing_form.is_valid() and images_form.is_valid() and order_form.is_valid():
                listing = listing_form.save(commit=False)
                listing.expiration_date = (timezone.now()
                                           + datetime.timedelta(days=90))
                if product.is_premium:
                    listing.premium_expiration = (timezone.now()
                                                  + datetime.timedelta(days=30))
                listing.product = product
                listing.save()
                for image in images:
                    RentListingImage.objects.create(
                        listing=listing,
                        images=image
                    )
                order = order_form.save(commit=False)
                order.order_total = product.price
                order.rent_listing = listing
                order.product = product
                order.save()
                return redirect('home')
            else:
                for error in listing_form.errors:
                    print('listing form error ***********')
                    print(error)
                for error in images_form.errors:
                    print('images form error ***********')
                    print(error)
                for error in order_form.errors:
                    print('order form error ***********')
                    print(error)
