from django.db import models

# Create your models here.


class Footer(models.Model):
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=255)
    yt_link = models.CharField(max_length=255)
    all_rights_msg = models.CharField(max_length=255)
    tuber_hire = models.CharField(max_length=255)
