from django.contrib import admin
from .models import UserRating

class RatingsAdmin(admin.ModelAdmin):

    list_display = (
        'user_profile', 
        'get_product_name', 
        'product_rating', 
        'rating_description'
        )

    search_fields = (
        'user_profile__user__username', 
        'product_id__name'
        )

    ordering = ('product_id',)

    def get_product_name(self, obj):
        return obj.product_id.name if obj.product_id else None
        
    get_product_name.short_description = 'Product Name'


admin.site.register(UserRating, RatingsAdmin)
