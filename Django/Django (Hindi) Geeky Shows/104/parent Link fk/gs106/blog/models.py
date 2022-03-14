from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Page(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    pageName = models.CharField(max_length=70)
    pageCat = models.CharField(max_length=70)
    pagePublishDate = models.DateField()

    def __str__(self):
        return self.user.username


class Like(Page):
    pata = models.OneToOneField(
        Page, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    likes = models.IntegerField()
