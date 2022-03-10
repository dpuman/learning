from atexit import register
from django.contrib import admin
from .models import Student, Employee


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuId', 'stuName', 'stuEmail',
                    'stuPassword', 'comments')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')


# admin.site.register(Student, StudentAdmin)
