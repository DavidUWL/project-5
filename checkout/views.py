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
        'stripe_public_key': 'pk_live_51OazHqCzje7ELh9qyyzI5uDg6hiG74G2wC4DxBlvvWbR4wy2xmXsgGmr7xPiYTgckdUahuGEvsSOQHhZkbxwVqVk00VBvu2DZV',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
