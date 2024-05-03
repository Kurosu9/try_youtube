# Generated by Django 5.0.4 on 2024-05-03 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notif_user_name', to='user.user'),
        ),
    ]