import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product, Category
from .forms import SaleListingForm, RentListingForm


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
    product = get_object_or_404(Product, pk=product_id)

    if product.category.name == 'sale':
        listing_form = SaleListingForm()
    elif product.category.name == 'rent':
        listing_form = RentListingForm()

    if request.method == 'POST':
        if product.category.name == 'sale':
            listing_form = SaleListingForm(request.POST, request.FILES)
            if listing_form.is_valid():
                listing = listing_form.save(commit=False)
                listing.expiration_date = (timezone.now()
                                           + datetime.timedelta(days=365))
                if product.is_premium:
                    listing.premium_expiration = (timezone.now()
                                                  + datetime.timedelta(days=30))
                listing.product = product
                listing.save()
                return redirect('home')
        elif product.category.name == 'rent':
            listing_form = RentListingForm(request.POST, request.FILES)
            if listing_form.is_valid():
                listing = listing_form.save(commit=False)
                listing.expiration_date = (timezone.now()
                                           + datetime.timedelta(days=90))
                if product.is_premium:
                    listing.premium_expiration = (timezone.now()
                                                  + datetime.timedelta(days=30))
                listing.product = product
                listing.save()
                return redirect('home')
            else:
                for error in listing_form.errors:
                    print(error)

    template = 'products/product_details.html'

    context = {
        'product': product,
        'listing_form': listing_form,
    }

    return render(request, template, context)
