from django.db import models
from user.models import User
from video.models import Video


class Comment(models.Model):
    user_name = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="comment_user_name")
    video = models.ForeignKey(to=Video, on_delete=models.SET_NULL, null=True, related_name="video")
    description = models.TextField(verbose_name='Description', max_length=1000)
    image = models.ImageField(verbose_name="Image", upload_to='video/')
    date = models.DateTimeField(verbose_name='Date')
    likes = models.PositiveIntegerField(verbose_name='Likes', default=0)
    replies_comment = models.PositiveIntegerField(verbose_name='NumberOfComments', default=0)

    def str(self):
        return self.name
