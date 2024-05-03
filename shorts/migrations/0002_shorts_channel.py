# Generated by Django 5.0.4 on 2024-05-03 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_delete_user_alter_playlist_channel'),
        ('shorts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorts',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shorts_channel', to='channel.channel'),
        ),
    ]