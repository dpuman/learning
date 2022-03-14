from django.contrib import admin

from blog.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Post._meta.get_fields()]
