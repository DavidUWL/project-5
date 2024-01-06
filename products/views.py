from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """ Returns all products regardless of query or sort """

    products= Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ Returns single product for product details page """ 

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_details.html', context)