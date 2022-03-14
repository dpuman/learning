from django.contrib import admin

from student.models import Student, MyStudent

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Student._meta.get_fields()]


@admin.register(MyStudent)
class MyStudentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Student._meta.get_fields()]
