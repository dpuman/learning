from atexit import register
from django.contrib import admin
from .models import Student, Employee, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuId', 'stuName', 'stuEmail',
                    'stuPassword', 'comments')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')


@admin.register(Teacher)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'studentName', 'teacherName', 'email', 'password')


# admin.site.register(Student, StudentAdmin)
