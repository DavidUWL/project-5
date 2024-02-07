from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.contrib.auth.models import User
from products.models import Product
from .forms import RatingsForm
from .models import UserRating


def get_user_rating(request, product_id):
    """
    Helper function to return and clean ratings form when called."
    """
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)

        form_data = {
            'user_profile': request.user,
            'product': product,
            'rating_description': request.POST['rating_description']
        }

        ratings_form = RatingsForm(form_data)
        if ratings_form.is_valid():

            ratings_form.save()
            return ratings_form


def collect_user_ratings(request):
    user = get_object_or_404(User, username=request.user.username)
    user_ratings = UserRating.objects.filter(user_profile__user=user)
    return user_ratings
