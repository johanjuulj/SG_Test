# Generated by Django 3.2.8 on 2024-11-20 11:37

from django.db import migrations
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_alter_task_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': [django.db.models.functions.text.Lower('taskName')]},
        ),
    ]
