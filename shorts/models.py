from django.db import models

class Shorts(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    description = models.TextField(verbose_name='Description', max_length=1000)
    link = models.TextField(verbose_name='Link', max_length=1000)
    views = models.PositiveIntegerField(verbose_name='Views', default=0)
    likes = models.PositiveIntegerField(verbose_name='Likes', default=0)
    comments = models.PositiveIntegerField(verbose_name='Comments', default=0)

    def str(self):
        return self.name
