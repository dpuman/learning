from django.contrib import admin
from .models import ExamCenter,MyExamCenter
# Register your models here.
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display=[f.name for f in ExamCenter._meta.get_fields()]

@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display=[f.name for f in MyExamCenter._meta.get_fields()]