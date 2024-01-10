from .models import Product

def highest_discount(request):
    discount_items = Product.objects.filter(discount__isnull=False)
    
    if discount_items.exists(): 
        discount_values = list(discount_items.values_list('discount', flat=True))
        highest_discount = max(discount_values)
    else:
        highest_discount = 0
    
    context = {
        'highest_discount': highest_discount,
    }

    return context