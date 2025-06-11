from django.contrib import admin
from .models import Product, CartItem, Comment


# Register your models here.
@admin.register( CartItem, Comment)
class Market(admin.ModelAdmin):
    pass


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_top')
    list_filter = [
        ("is_top", admin.BooleanFieldListFilter)
    ]
    search_fields = ('name', 'name')
    actions = ['my_custom_action']
    def my_custom_action(self, request, queryset):
        queryset.update(is_top=True)