from django.urls import path
from .views import home, user_logout, add_product, product_lists_admin, register, login_view, set_cookies, \
    check_cookies, password_reset_request

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('add/', add_product, name='add_product'),
    path('lists/', product_lists_admin, name='product_lists_admin'),
    path('set', set_cookies),
    path('check', check_cookies),
    path('reset1', password_reset_request)
]