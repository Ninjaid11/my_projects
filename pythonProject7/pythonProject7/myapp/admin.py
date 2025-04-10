from django.contrib import admin
from .models import Student, Group, LibraryCard, BookCheckout, Literature
# Register your models here.


admin.site.register(Student)
admin.site.register(Group)
admin.site.register(LibraryCard)
admin.site.register(BookCheckout)
admin.site.register(Literature)