from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from decimal import Decimal
from products.models import Product


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        messages.success(request, f'{product.name} added to your cart.')
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'{product.name} added to your cart.')
            else:
                cart[item_id]['items_by_size'] = quantity
                messages.success(request, f'{product.name} added to your cart.')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f"{product.name}'s quantity to {cart[item_id]}.")
        else:
            cart[item_id] = quantity
            messages.success(request, f'{product.name} added to your cart.')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Product, pk=item_id)

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                messages.success(request, f"Removed {product.name} from cart.")
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f"{product.name}'s quantity to {cart[item_id]}.")
        else:
            cart.pop(item_id)
            messages.success(request, f"Removed {product.name} from cart.")

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    product = get_object_or_404(Product, pk=item_id)

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                messages.success(request, f"Removed {product.name} from cart.")
        else:
            cart.pop(item_id)
            messages.success(request, f"Removed {product.name} from cart.")


        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
