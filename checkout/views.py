from django.shortcuts import render, redirect, reverse, get_object_or_404 # NOQA
from django.contrib import messages # NOQA
from django.conf import settings # NOQA
import stripe # NOQA
from cart.contexts import cart_contents
from .forms import PurchaseForm

from products.models import Product
from .models import OrderLineItem, Purchase


def view_checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        purchase_form = PurchaseForm(form_data)

        if purchase_form.is_valid(): # NOQA
            purchase = purchase_form.save(commit=False)
            purchase.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=purchase,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=purchase,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "It looks like that item isn't in our database, please try again."
                        )
                    )
                    purchase.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info']= 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[purchase.order_number]))
        else:
            messages.error(request,  "We can't process your form, have a look and try again.")

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "You haven't added any items.")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    if not stripe_public_key:
        messages.warning(request, 'Enter your stripe key.')

    purchase_form = PurchaseForm()
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)



def checkout_success(request, order_number):
    save_info = request.session.get('save-info')
    order = get_object_or_404(Purchase, order_number=order_number)
    messages.success(request,
        f'Your order has been completed. Your order number is #{order_number}'
        )
    if 'cart' in request.session:
        del request.session['cart']
    context = {
        'order': order
    }
    return render(request, 'checkout/checkout_success.html', context)