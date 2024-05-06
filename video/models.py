from django.db import models
from user.models import User
from channel.models import Channel, Playlist
from datetime import datetime

class Video(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    description = models.TextField(verbose_name='Description', max_length=1000)
    image = models.ImageField(verbose_name="Image", upload_to='video/')
    link = models.TextField(verbose_name='Link', max_length=1000)
    views = models.PositiveIntegerField(verbose_name='Views', default=0)
    likes = models.PositiveIntegerField(verbose_name='Likes', default=0)
    comments = models.PositiveIntegerField(verbose_name='Comments', default=0)
    channel = models.ForeignKey(to=Channel, on_delete=models.SET_NULL, null=True, related_name="video_channel")
    playlist = models.ForeignKey(to=Playlist, on_delete=models.SET_NULL, null=True, related_name="video_playlist")
    date = models.DateTimeField(verbose_name='Date', default=datetime.now)

    def str(self):
        return self.title
