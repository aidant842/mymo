import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.conf import settings
from .models import Product, Category
from .forms import SaleListingForm, RentListingForm, SaleImageForm, RentImageForm
from listings.models import SaleListingImage, RentListingImage
from checkout.forms import OrderForm
from checkout.models import Order

import stripe


def products_view(request):
    """ A view to return the products """

    """ Filter by category """

    selected_category = request.GET.get('category', None)

    if selected_category:
        products = Product.objects.filter(category__name=selected_category)
    else:
        products = Product.objects.filter(category__name='sale')

    template = 'products/products.html'

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, template, context)


def product_detail(request, product_id):
    """ A view to return the form to fill out to create a listing """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    product = get_object_or_404(Product, pk=product_id)
    order_form = OrderForm()

    stripe_total = product.price
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    if product.category.name == 'sale':
        listing_form = SaleListingForm()
        images_form = SaleImageForm()
    elif product.category.name == 'rent':
        listing_form = RentListingForm()
        images_form = RentImageForm()

    if not stripe_public_key:
        print('********* ALERT STRIPE PUBLIC KEY NOT SET IN ENVIRON *************')

    template = 'products/product_details.html'

    context = {
        'product': product,
        'listing_form': listing_form,
        'images_form': images_form,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

