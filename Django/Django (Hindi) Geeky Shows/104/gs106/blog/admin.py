from django.contrib import admin
from .models import Page
# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):

    list_display = [f.name for f in Page._meta.get_fields()]
