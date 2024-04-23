# Generated by Django 5.0.4 on 2024-04-23 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
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
        migrations.AddField(
            model_name='playlist',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel', to='product.channel'),
        ),
    ]