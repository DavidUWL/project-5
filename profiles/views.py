from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ratings.views import collect_user_ratings
from checkout.models import Purchase
from .models import UserProfile
from .forms import UserProfileForm
from ratings.models import UserRating

@login_required
def view_profile(request):
    user = request.user

    template = 'profiles/profile.html'
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(request.POST, instance=profile)
    purchases = profile.purchases.all()
    purchases = purchases.order_by('-date')
    user_ratings = UserRating.objects.filter(user_profile=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
        'purchases': purchases,
        'user_ratings': user_ratings,
    }

    return render(request, template, context)

@login_required
def delete_user_profile(request):
    if request.method == 'POST':
        user_profile = request.user.userprofile
        user_profile.delete()
        messages.success(request, 'Your saved details have been deleted.')

    return render(request, 'profile.html')


def purchase_history(request, order_number):
    purchase = get_object_or_404(Purchase, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'purchase': purchase,
    }

    return render(request, template, context)

def delete_user_rating(request, rating_id):
    if request.method == 'POST':
        user_rating = get_object_or_404(UserRating, pk=rating_id)
        user_rating.delete()
        messages.success(request, 'Your rating has been deleted.')
        return redirect('view_profile')
    else:
        messages.warning(request, 'Deletion was not confirmed.')
    return render(request, 'profile.html')

