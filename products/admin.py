from django.contrib import admin
from .models import Product, Category, Subcategory, Technology

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sku',
        'name',
        'category',
        'subcategory',
        'price',
        'discount',
        'rating',
        'image',
    )
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )

class TechnologyAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Technology, TechnologyAdmin)
