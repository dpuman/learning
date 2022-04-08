from django.contrib import admin
from .models import Singer, Song
# Register your models here.


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Song._meta.get_fields()]
