from django.urls import path
from .views import home, user_logout, add_product, product_lists_admin

urlpatterns = [
    path('', home, name='home'),
    path('logout/', user_logout, name='logout'),
    path('add/', add_product, name='add_product'),
    path('lists/', product_lists_admin, name='product_lists_admin'),
]