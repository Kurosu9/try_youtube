from django.db import models

class Comment(models.Model):
    user_name = models.CharField(verbose_name='Title', max_length=100)
    description = models.TextField(verbose_name='Description', max_length=1000)
    image = models.ImageField(verbose_name="Image", upload_to='video/')
    date = models.DateTimeField(verbose_name='Date')
    likes = models.PositiveIntegerField(verbose_name='Likes', default=0)
    replies_comment = models.TextField(verbose_name='Comments', max_length=1000)

    def str(self):
        return self.name
