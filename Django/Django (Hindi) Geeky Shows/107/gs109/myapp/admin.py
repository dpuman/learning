from django.contrib import admin

from myapp.models import Page, Post, Song

# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):

    list_display = [f.name for f in Page._meta.get_fields()]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Post._meta.get_fields()]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_duration', 'written_by']
