from django.shortcuts import (
    render, 
    get_object_or_404,
)
from products.models import Product
from .models import UserRating
from .forms import RatingsForm


def get_user_rating(request, product_id):
    if request.method == 'GET':
        ratings_form = RatingsForm()
        return ratings_form

    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)

        print(f'product.id == {product.id}')
        print(request.POST)

        
        form_data = {
            'user_profile': request.user.username,
            'product': product.id,
            'product_name': product.name,
            'rating_description': request.POST['rating_description']
        }

        ratings_form = RatingsForm(form_data)

        if ratings_form.is_valid():
            ratings_form.save()
            return ratings_form
