from django.db import models

class User(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=30)
    last_name = models.CharField(verbose_name="Last Name", max_length=30)
    username = models.CharField(verbose_name="Username", max_length=30, unique=True)
    password = models.CharField(verbose_name="Password", max_length=20)
    email = models.EmailField(verbose_name="Email", max_length=30)

    def __str__(self):
        return self.name

class Notification(models.Model):
    title = models.CharField(verbose_name="Title", max_length=250)
    channel_name = models.CharField(verbose_name="Channel Name", max_length=50)
    channel_ava = models.ImageField(verbose_name="Ava", upload_to='user/')
    number_of_videos = models.PositiveIntegerField(verbose_name='NumberOfVideos')
    video_image = models.ImageField(verbose_name="Ava", upload_to='user/')
    date = models.CharField(verbose_name="Date", max_length=50)

    def __str__(self):
        return self.name
    

