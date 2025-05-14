from django.urls import path
from .views import home, user_logout, add_product, product_lists_admin, register, login_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('add/', add_product, name='add_product'),
    path('lists/', product_lists_admin, name='product_lists_admin'),
]