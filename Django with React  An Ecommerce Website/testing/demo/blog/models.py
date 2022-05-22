from django.db import models

# Create your models here.


class user(models.Model):
    image = models.ImageField(blank=True, null=True)
