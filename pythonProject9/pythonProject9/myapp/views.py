from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


# Create your views here.
def get_all_product(request):
    all_product = Product.objects.all()
    paginator = Paginator(all_product, 1)

    page_num = request.GET.get("page", 1)
    page = paginator.get_page(page_num)

    context = {
        "page": page,
        "all_product": page.object_list,
    }

    return render(request, "products.html", context)
