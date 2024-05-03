from django.db import models
from channel.models import Channel

class Shorts(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    description = models.TextField(verbose_name='Description', max_length=1000)
    link = models.TextField(verbose_name='Link', max_length=1000)
    views = models.PositiveIntegerField(verbose_name='Views', default=0)
    likes = models.PositiveIntegerField(verbose_name='Likes', default=0)
    comments = models.PositiveIntegerField(verbose_name='Comments', default=0)
    channel = models.ForeignKey(to=Channel, on_delete=models.SET_NULL, null=True, related_name="shorts_channel")

    def str(self):
        return self.name
