from django.contrib import admin
from .models import Category, Material, Size, Brand, Color, Review, Product

admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Review)
admin.site.register(Product)