from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import ProductForm
from .models import Product


# views.py

def home(request):
    top_products = Product.objects.filter(is_top=True)
    main_products = Product.objects.filter(is_top=False)
    return render(request, 'home.html', {
        'top_products': top_products,
        'main_products': main_products,
    })


def user_logout(request):
    logout(request)
    return redirect('/')


def add_product(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})


def product_lists_admin(request):
    if not request.user.is_superuser:
        return redirect('home')

    top = Product.objects.filter(is_top=True)
    main = Product.objects.filter(is_top=False)

    return render(request, 'product_lists.html', {
        'top': top,
        'main': main
    })