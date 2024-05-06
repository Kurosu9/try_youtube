from django.db import models
from user.models import User

class Channel(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    tag = models.CharField(verbose_name="Tag", max_length=50)
    description = models.CharField(verbose_name="Description", max_length=250)
    link = models.CharField(verbose_name="Link", max_length=250)
    head_image = models.ImageField(verbose_name="Image", upload_to='channel/')
    ava = models.ImageField(verbose_name="Ava", upload_to='channel/')
    subscribers = models.PositiveIntegerField(verbose_name='Subscribers')
    number_of_videos = models.PositiveIntegerField(verbose_name='NumberOfVideos')
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="channel_owner")


    def str(self):
        return self.name
    
class Playlist(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    image = models.ImageField(verbose_name="Image", upload_to='playlist/')
    number_of_videos = models.PositiveIntegerField(verbose_name='NumberOfVideos')
    channel = models.ForeignKey(to=Channel, on_delete=models.SET_NULL, null=True, related_name="playlist_channel")
    
    def str(self):
        return self.name