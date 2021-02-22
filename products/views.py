from django.shortcuts import render, get_object_or_404
from .models import Product, Category


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

    template = 'products/product_details.html'

    context = {
        'product': product,
    }

    return render(request, template, context)
