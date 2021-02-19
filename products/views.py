from django.shortcuts import render
from .models import Product, Category


def products_view(request):
    """ A view to return the products """
    template = 'products/products.html'

    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, template, context)
