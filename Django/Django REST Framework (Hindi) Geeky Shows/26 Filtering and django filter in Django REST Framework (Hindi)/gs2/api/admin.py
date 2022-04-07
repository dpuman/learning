from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)
class StudentModel(admin.ModelAdmin):
    list_display = [f.name for f in Student._meta.get_fields()]
