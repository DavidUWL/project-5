from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import PurchaseForm

def view_checkout(request):
    cart = request.session.get('cart', {})
    if not cart: 
        messages.error(request, "You haven't added any items.")
        return redirect(reverse('products'))

    purchase_form = PurchaseForm()
    template = './checkout.html'
    context = {
        'purchase_form': purchase_form,
    }

    return render(request, template, context)
