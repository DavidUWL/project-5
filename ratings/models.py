from django.db import models
from products.models import Product
from profiles.models import UserProfile


class UserRating(models.Model):

    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        )

    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='ratings'
        )

    product_rating = models.IntegerField(
        null=True,
        blank=True,
        default=0
    )

    rating_description = models.CharField(
        max_length=127,
        null=True,
        blank=True,
    )
