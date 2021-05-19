import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from .forms import SaleListingForm, RentListingForm, SaleImageForm, RentImageForm
from listings.models import SaleListingImage, RentListingImage, SaleListing, RentListing
from checkout.forms import OrderForm
from checkout.models import Order
from profiles.models import UserProfile

import stripe


def products_view(request):
    """ A view to return the products """

    user = UserProfile.objects.get(user=request.user)

    if 'product_id' in request.session:
        del request.session['product_id']

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
        'categories': categories,
        'user': user,
    }
    return render(request, template, context)


@login_required
def product_detail(request, product_name, product_id):
    """ A view to return the form to fill out to create a listing """
    product = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)

    if product.category.name == 'sale':
        if 'listing_id' in request.session:
            listing_id = request.session.get('listing_id')
            try:
                listing = SaleListing.objects.get(pk=listing_id)
            except SaleListing.DoesNotExist:
                messages.error(request, 'An error occured, please try again.')
                del request.session['listing_id']
                return redirect('products')
            listing_form = SaleListingForm(instance=listing)
            images_form = SaleImageForm(instance=listing)
        else:
            listing_form = SaleListingForm()
            images_form = SaleImageForm()
    elif product.category.name == 'rent':
        if 'listing_id' in request.session:
            listing_id = request.session.get('listing_id')
            try:
                listing = RentListing.objects.get(pk=listing_id)
            except RentListing.DoesNotExist:
                messages.error(request, 'An error occured, please try again.')
                del request.session['listing_id']
                return redirect('products')
            listing_form = RentListingForm(instance=listing)
            images_form = RentImageForm(instance=listing)
        else:
            listing_form = RentListingForm()
            images_form = RentImageForm()

    template = 'products/product_details.html'

    context = {
        'product': product,
        'listing_form': listing_form,
        'images_form': images_form,
        'user': user,
    }

    return render(request, template, context)

