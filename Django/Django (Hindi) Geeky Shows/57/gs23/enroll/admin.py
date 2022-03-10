from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuId', 'stuName', 'stuEmail',
                    'stuPassword', 'comments')


# admin.site.register(Student, StudentAdmin)
