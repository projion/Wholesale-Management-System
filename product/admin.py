from django.contrib import admin
from .models import Category, Product
# Register your models here.

# class ProductCatagoryInfo(admin.ModelAdmin):
#     list_display = ['category_id', 'category_name']
class ProductList(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'price', 'status', 'quantity', 'category_name']

# admin.site.register(Category, ProductCatagoryInfo)
admin.site.register(Category)
admin.site.register(Product, ProductList)
