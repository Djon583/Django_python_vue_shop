from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
  title = models.CharField(max_length=80)
  description = models.TextField(max_length=300)
  url = models.URLField()
  category = models.CharField(max_length=50)
  subcategory = models.TextField(max_length=50)
  author = models.TextField(max_length=50)

class Rating(models.Model):
  video = models.ForeignKey(Video, on_delete=models.CASCADE)
  user = models.ForeignKey (User, on_delete=models.CASCADE)
  stars = models.IntegerField()
  comments = models.TextField(max_length=300)

  class Meta:
    unique_together = (('user','video'),)
    index_together = (('user','video'),)