from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .forms import ProductForm, RegisterForm
from .models import Product, CartItem
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import login as auth_login
from django.http import HttpResponse

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


def set_cookies(request):
    response = HttpResponse("Cookies were set")
    response.set_cookie('mycookie', 'goiteens', max_age=10)
    return response


def check_cookies(request):
    cookies = request.COOKIES

    if "mycookie" not in cookies:
        return HttpResponse("403 Forbidden")

    value = cookies["mycookie"]
    return HttpResponse(f"Cookie value: {value}")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset_email.html"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except Exception:
                        return HttpResponse('Invalid header found.')
                    return redirect ("registration/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})


def delete_product(request, product_id):
    if not request.user.is_superuser:
        return redirect('home')

    try:
        product = Product.objects.get(id=product_id)
        CartItem.objects.filter(product=product).delete()
        product.delete()
    except Product.DoesNotExist:
        pass

    return redirect('home')


def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.count += 1
    cart_item.save()

    return redirect('home')


def remove_from_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
    cart_item.delete()

    return redirect('cart')


def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})