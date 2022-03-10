from django.db import models

# Create your models here.


class Student(models.Model):
    stuId = models.IntegerField()
    stuName = models.CharField(max_length=70)
    stuEmail = models.EmailField(max_length=70)
    stuPassword = models.CharField(max_length=70)
    comments = models.TextField(blank=True, null=True, default='No Comments')

    def __str__(self):
        # return str(self.stuId)
        return self.stuName


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=100)


class Teacher(models.Model):
    studentName = models.CharField(max_length=50)
    teacherName = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=100)
