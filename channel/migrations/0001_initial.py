# Generated by Django 5.0.4 on 2024-05-03 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('tag', models.CharField(max_length=50, verbose_name='Tag')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('link', models.CharField(max_length=250, verbose_name='Link')),
                ('head_image', models.ImageField(upload_to='channel/', verbose_name='Image')),
                ('ava', models.ImageField(upload_to='channel/', verbose_name='Ava')),
                ('subscribers', models.PositiveIntegerField(verbose_name='Subscribers')),
                ('number_of_videos', models.PositiveIntegerField(verbose_name='NumberOfVideos')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('image', models.ImageField(upload_to='playlist/', verbose_name='Image')),
                ('number_of_videos', models.PositiveIntegerField(verbose_name='NumberOfVideos')),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel', to='channel.channel')),
            ],
        ),
    ]
