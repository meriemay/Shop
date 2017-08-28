from django.contrib.auth.models import Permission, User
from django.db import models
from django.conf import settings
from django.utils import timezone


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    album_name = models.CharField(max_length=250)
    album_logo = models.FileField(null=True)
    album_description = models.TextField(max_length=250, default=None)
    
    def __str__(self):
        return self.album_name 


class Picture(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    picture_description = models.TextField(max_length=250, default=None)
    pic = models.FileField(null=True)
   
    def __str__(self):
        return self.picture_description

   

