from django.db import models
from decimal import Decimal

class Category(models.Model): 

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name


class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subcategories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name


class Technology(models.Model):

    class Meta:
        verbose_name_plural = 'Technologies'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('Subcategory', null=True, blank=True, on_delete=models.SET_NULL)
    technology = models.ForeignKey('Technology', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    size = models.CharField(max_length=254, null=True, blank=True)
    models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property  
    def calculate_discount_price(self): 
        discount_percentage = Decimal(self.discount) / Decimal(100)
        discounted_amount = self.price * discount_percentage
        discounted_price = self.price - discounted_amount
        return round(discounted_price, 2)
