from django.contrib import admin
from .models import Blog
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Blog._meta.get_fields()]
