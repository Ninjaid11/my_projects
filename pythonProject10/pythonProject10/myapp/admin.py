from django.contrib import admin
from .models import Product, TopProduct, MainProduct

# Register your models here.
admin.site.register(Product)
admin.site.register(TopProduct)
admin.site.register(MainProduct)
