from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from checkout.models import Purchase
from .models import UserProfile
from .forms import UserProfileForm


def view_profile(request):
    template = 'profiles/profile.html'
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(request.POST, instance=profile)
    purchases = profile.purchases.all()
    purchases = purchases.order_by('-date')

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
    }

    return render(request, template, context)


def purchase_history(request, order_number):
    purchase = get_object_or_404(Purchase, order_number=order_number)
    
    template = 'checkout/checkout_success.html'
    context = {
        'purchase': purchase,
    }

    return render(request, template, context)