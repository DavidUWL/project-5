from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    grand_total = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)

            if product.discount:
                total += item_data * product.calculate_discount_price
            else:
                total += item_data * product.price

            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            for size, quantity in item_data['items_by_size'].items():
                product = get_object_or_404(Product, pk=item_id)

                if product.discount:
                    total += quantity * product.calculate_discount_price
                else:
                    total += quantity * product.price

                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
