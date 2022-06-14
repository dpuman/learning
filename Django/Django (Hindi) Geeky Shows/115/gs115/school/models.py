from django.urls import reverse
from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    course = models.CharField(max_length=70)

    # to redirect after data is saved
    # def get_absolute_url(self):
    #     return reverse("thankyou")

    # to redirect after data is saved with details

    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})
