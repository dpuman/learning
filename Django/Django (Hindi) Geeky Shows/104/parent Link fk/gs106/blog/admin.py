from django.contrib import admin
from .models import Page, Like
# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Page._meta.get_fields()]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Like._meta.get_fields()]
