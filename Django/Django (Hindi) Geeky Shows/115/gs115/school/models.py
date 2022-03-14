from django.urls import reverse
from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    course = models.CharField(max_length=70)

    # def get_absolute_url(self):
    #     return reverse("thankyou")

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
