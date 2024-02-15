from django.contrib import admin
from .models import UserRating


class RatingsAdmin(admin.ModelAdmin):

    list_display = (
        'user_profile',
        'product_rating',
        'rating_description'
        )

    search_fields = (
        'user_profile__user__username',
        'product_id__name'
        )

    ordering = ('product_id',)


admin.site.register(UserRating, RatingsAdmin)
