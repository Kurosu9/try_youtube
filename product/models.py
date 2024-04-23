from django.db import models

class Channel(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    tag = models.CharField(verbose_name="Tag", max_length=50)
    description = models.CharField(verbose_name="Description", max_length=250)
    link = models.CharField(verbose_name="Link", max_length=250)
    head_image = models.ImageField(verbose_name="Image", upload_to='channel/')
    ava = models.ImageField(verbose_name="Ava", upload_to='channel/')
    subscribers = models.PositiveIntegerField(verbose_name='Subscribers')
    number_of_videos = models.PositiveIntegerField(verbose_name='NumberOfVideos')

    def __str__(self):
        return self.name
    
class Playlist(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    image = models.ImageField(verbose_name="Image", upload_to='playlist/')
    number_of_videos = models.PositiveIntegerField(verbose_name='NumberOfVideos')
    channel = models.ForeignKey(to=Channel, on_delete=models.SET_NULL, null=True, related_name="channel")
    
    def __str__(self):
        return self.name

    
# class Video(models.Model):
#     playlist = models.ForeignKey(to=Playlist, on_delete=models.SET_NULL, null=True, related_name="playlist")
#     channel = models.ForeignKey(to=Channel, on_delete=models.SET_NULL, null=True, related_name="channel")
#     title = models.CharField(verbose_name='Title', max_length=100)
#     description = models.TextField(verbose_name='Description')
#     image = models.ImageField(verbose_name="Image", upload_to='video/')
#     link = models.TextField(verbose_name='Link')
#     views = models.PositiveIntegerField(verbose_name='Views')
#     likes = models.PositiveIntegerField(verbose_name='Likes')
#     comments = models.PositiveIntegerField(verbose_name='Comments')

#     def __str__(self):
#         return self.name
