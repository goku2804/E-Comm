from django.contrib import admin

# Register your models here.
# products/admin.py
from .models import Category, Product
admin.site.register(Category)
admin.site.register(Product)
