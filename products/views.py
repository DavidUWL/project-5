from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q 
from django.db.models.functions import Lower
from .models import Product
from ratings.views import get_user_rating



def all_products(request):
    """ Returns all products regardless of query or sort """

    products = Product.objects.all()
    query = None
    categories = None
    subcategories = None
    technologies = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            if 'subcategory' in request.GET:
                subcategory = request.GET['subcategory']
                category_query = Q(category__name__icontains=category)
                subcategory_query = Q(subcategory__name__icontains=subcategory)
                products = products.filter(category_query & subcategory_query)
            else:
                products = products.filter(category__name__icontains=category)

        if not 'category' in request.GET and 'subcategory' in request.GET:
            subcategory = request.GET['subcategory']
            subcategory_query = Q(subcategory__name__icontains=subcategory)
            products = products.filter(subcategory_query)

        if 'technology' in request.GET: 
            technology = request.GET['technology']
            technology_query = Q(technology__name__icontains=technology)
            products = products.filter(technology_query)

        if 'discount' in request.GET: 
            discount = request.GET['discount']
            discount_query = Q(discount__isnull=False)
            products = products.filter(discount_query)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "you didn't enter any text to search!")

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search-term': query,
        'current_categories': categories,
        'current_subcategories': subcategories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ Returns single product for product details page """
    product = get_object_or_404(Product, pk=product_id)
    ratings_form = get_user_rating(request, product.id)

    if ratings_form.is_valid():
        ratings_form.save()

    print(f" in product view: {ratings_form}")
    context = {
        'product': product,
        'ratings_form': ratings_form,
    }
    return render(request, 'products/product_details.html', context)