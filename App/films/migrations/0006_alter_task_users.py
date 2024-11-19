# Generated by Django 3.2.8 on 2024-11-19 19:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_auto_20241119_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='users',
           
        ),
        migrations.AddField(
            model_name='task',
            name='users',
           field=models.ManyToManyField(related_name='tasks', through="films.UserTasks", to=settings.AUTH_USER_MODEL),
        ),
        
    ]
