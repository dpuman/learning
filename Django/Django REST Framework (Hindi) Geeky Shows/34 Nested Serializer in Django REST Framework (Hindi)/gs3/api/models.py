from django.db import models

# Create your models here.


class Singer(models.Model):
    genders = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=70)
    gender = models.CharField(max_length=70, choices=genders)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(
        Singer, on_delete=models.CASCADE, related_name='sungby')
    duration = models.IntegerField()

    def __str__(self):
        return self.title
