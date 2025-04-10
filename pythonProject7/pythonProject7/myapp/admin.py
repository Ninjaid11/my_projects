from django.contrib import admin
from .models import Student, Group, LibraryCard, BookCheckout, Literature
# Register your models here.


# Регистрируем модели для отображения в админке
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(LibraryCard)
admin.site.register(BookCheckout)
admin.site.register(Literature)