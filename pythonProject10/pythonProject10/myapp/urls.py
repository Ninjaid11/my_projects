from django.urls import path
from .views import home, register, login_view, user_logout, add_product, product_lists_admin, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add/', add_product, name='add_product'),
    path('lists/', product_lists_admin, name='product_lists_admin'),
    path('product/<int:id>/', product_detail, name='product_detail'),
]