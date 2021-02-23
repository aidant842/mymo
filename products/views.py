import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product, Category
from .forms import SaleListingForm


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

    sale_listing_form = SaleListingForm()

    if request.method == 'POST':
        sale_listing_form = SaleListingForm(request.POST, request.FILES)

        if sale_listing_form.is_valid():
            listing = sale_listing_form.save(commit=False)
            listing.expiration_date = timezone.now() + datetime.timedelta(days=365)
            listing.product = product
            listing.save()
            return redirect('home')

    template = 'products/product_details.html'

    context = {
        'product': product,
        'sale_listing_form': sale_listing_form,
    }

    return render(request, template, context)
