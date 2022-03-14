from django.contrib import admin

from school.models import Contractor, Student, Teacher

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.get_fields()]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Teacher._meta.get_fields()]


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contractor._meta.get_fields()]
