from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    return render(request, "base.html")