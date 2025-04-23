from django.shortcuts import render
from .models import Product


# Create your views here.
def get_all_product(request):
    context = {
        'all_product': Product.objects.all()
    }

    return render(request, "products.html", context)