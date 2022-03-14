from django.contrib import admin
from .models import ExamCenter, Student
# Register your models here.


@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ExamCenter._meta.get_fields()]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Student._meta.get_fields()]
