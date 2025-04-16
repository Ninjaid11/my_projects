from django.shortcuts import render, redirect
from .models import Product, Basket
# Create your views here.


def product_list(request):
    products = Product.objects.all()
    return render(request, 'list.html', {'products': products})


def basket(request):
    baskets = Basket.objects.all()
    return render(request, 'basket.html', {'baskets': baskets})