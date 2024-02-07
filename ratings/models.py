from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class UserRating(models.Model):

    user_profile = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        )

    product = models.ForeignKey(
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
