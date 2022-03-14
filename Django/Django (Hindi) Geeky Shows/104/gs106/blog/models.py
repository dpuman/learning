from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Page(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    # user = models.OneToOneField(
    #     User, on_delete=models.PROTECT, primary_key=True)
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': True})
    pageName = models.CharField(max_length=70)
    pageCat = models.CharField(max_length=70)
    pagePublishDate = models.DateField()
