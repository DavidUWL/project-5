from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Subcategory

# Create your views here.

def all_products(request):
    """ Returns all products regardless of query or sort """

    products = Product.objects.all()
    query = None
    categories = None
    subcategories = None

    if request.GET:
        
        if 'category' in request.GET:
            category = request.GET['category']
            print(category)
            if 'subcategory' in request.GET:
                subcategory = request.GET['subcategory']
                print(subcategory)
                category_query = Q(category__name__icontains=category)
                subcategory_query = Q(subcategory__name__icontains=subcategory)
                products = products.filter(category_query & subcategory_query)
            else:
                products = products.filter(category__name__icontains=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "you didn't enter any text to search!")
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)


    context = {
        'products': products,
        'search-term': query,
        'current_categories': categories,
        'current_subcategories': subcategories,
    }
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ Returns single product for product details page """ 

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_details.html', context)



