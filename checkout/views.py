import json
import stripe
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from cart.contexts import cart_contents
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from products.models import Product
from .forms import PurchaseForm
from .models import OrderLineItem, Purchase


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'username': request.user,
            'save_info': request.POST.get('save_info')
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'We could not process your request.')
        return HttpResponse(content=e, status=400)


@login_required
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

        if purchase_form.is_valid():  # NOQA
            purchase = purchase_form.save(commit=False)
            purchase.save()
            pid = request.POST.get('client_secret').split('_secret')[0]
            purchase.stripe_pid = pid
            purchase.original_cart = json.dumps(cart)
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
                    messages.error(
                        request,
                        (
                            "It looks like that item isn't in our database, \
                            please try again."
                        )
                    )
                    purchase.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[purchase.order_number])
            )
        else:
            messages.error(
                request,
                "We can't process your form, have a look and try again."
            )

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

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                purchase_form = PurchaseForm(initial={
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })

            except UserProfile.DoesNotExist:
                purchase_form = PurchaseForm()
        else:
            purchase_form = PurchaseForm()

    if not stripe_public_key:
        messages.warning(request, 'Enter your stripe key.')

    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


@login_required
def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    purchase = get_object_or_404(Purchase, order_number=order_number)

    profile = UserProfile.objects.get(user=request.user)
    purchase.user_profile = profile
    purchase.save()

    if save_info:
        profile_data = {
            'default_phone_number': purchase.phone_number,
            'default_country': purchase.country,
            'default_postcode': purchase.postcode,
            'default_town_or_city': purchase.town_or_city,
            'default_street_address1': purchase.street_address1,
            'default_street_address2': purchase.street_address2,
            'default_county': purchase.county,
        }

        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(
        request,
        f'Your order has been completed. Your order number is: #{order_number}'
    )
    if 'cart' in request.session:
        del request.session['cart']
    context = {
        'purchase': purchase
    }
    return render(request, 'checkout/checkout_success.html', context)
