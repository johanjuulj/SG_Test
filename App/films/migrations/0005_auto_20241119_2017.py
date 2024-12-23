# Generated by Django 3.2.8 on 2024-11-19 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_auto_20241119_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': [django.db.models.functions.text.Lower('name')]},
        ),
        migrations.CreateModel(
            name='UserTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=1)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
