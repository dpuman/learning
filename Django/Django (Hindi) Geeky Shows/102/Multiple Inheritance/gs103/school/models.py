from django.db import models

# Create your models here.


class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)

    def __str__(self):
        return self.cname


class Student(ExamCenter):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    def __str__(self):
        return self.name
