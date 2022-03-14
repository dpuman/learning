from django.db import models
from .manager import CustomManager
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()


class MyStudent(Student):
    class Meta:
        proxy = True

    student = CustomManager()

    ordering = ['roll']
