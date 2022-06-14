from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Page(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="mypage")
    pageName = models.CharField(max_length=70)
    pageCat = models.CharField(max_length=70)
    pagePublishDate = models.DateField()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()


class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=70)
    song_duration = models.IntegerField()

    def written_by(self):
        return ','.join([str(u) for u in self.user.all()])
