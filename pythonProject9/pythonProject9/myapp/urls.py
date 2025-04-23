from django.urls import path
from .views import get_all_product

urlpatterns = [
    path("", get_all_product)
]