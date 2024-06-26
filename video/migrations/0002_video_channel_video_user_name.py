# Generated by Django 5.0.4 on 2024-05-03 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_delete_user_alter_playlist_channel'),
        ('user', '0003_notification_user_name'),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_channel', to='channel.channel'),
        ),
        migrations.AddField(
            model_name='video',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_user_name', to='user.user'),
        ),
    ]
