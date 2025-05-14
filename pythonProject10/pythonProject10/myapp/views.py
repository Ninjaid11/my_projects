from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import ProductForm, RegisterForm
from .models import Product
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


# views.py

def home(request):
    top_products = Product.objects.filter(is_top=True)
    main_products = Product.objects.filter(is_top=False)
    return render(request, 'home.html', {
        'top_products': top_products,
        'main_products': main_products,
    })


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


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