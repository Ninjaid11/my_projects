from django.urls import path
from .views import product_list, basket

urlpatterns = [
    path("list", product_list),
    path("basket", basket),
]