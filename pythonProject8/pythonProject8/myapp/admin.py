from django.contrib import admin
from .models import Product, Basket


class BasketAdmin(admin.ModelAdmin):
    filter_horizontal = ('product',)


admin.site.register(Product)
admin.site.register(Basket, BasketAdmin)