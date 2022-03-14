from django.contrib import admin

from blog.models import Song

# Register your models here.


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_duration', 'written_by']
