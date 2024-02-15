from django.contrib import admin
from .models import Purchase, OrderLineItem


class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class PurchaseAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total', 'grand_total',
                       'stripe_pid', 'original_cart')

    fields = ('order_number', 'date', 'full_name', 'email',
              'phone_number', 'country', 'postcode', 'town_or_city',
              'street_address1', 'street_address2', 'county',
              'delivery_cost', 'order_total', 'grand_total')

    list_display = ('order_number', 'date', 'full_name',
                    'delivery_cost', 'order_total', 'grand_total')

    ordering = ('-date',)


admin.site.register(Purchase, PurchaseAdmin)