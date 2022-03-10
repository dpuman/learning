from django.db import models

# Create your models here.


class Student(models.Model):
    stuId = models.IntegerField()
    stuName = models.CharField(max_length=70)
    stuEmail = models.EmailField(max_length=70)
    stuPassword = models.CharField(max_length=70)
    comments = models.TextField(blank=True, null=True, default='No Comments')
