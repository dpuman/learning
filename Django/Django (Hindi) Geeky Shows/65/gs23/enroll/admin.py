from atexit import register
from django.contrib import admin
from .models import Student, employee


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuId', 'stuName', 'stuEmail',
                    'stuPassword', 'comments')


@admin.register(employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')


# admin.site.register(Student, StudentAdmin)
