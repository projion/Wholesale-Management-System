from django.shortcuts import render
# Create your views here.
from .models import Product
def product1(request):
    productlist= Product.objects.all()
    return render(request, 'product/productList.html', { 'productlist': productlist })
