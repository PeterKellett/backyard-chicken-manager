# Generated by Django 4.0.1 on 2022-02-28 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regular_tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eggcollection',
            name='image_url',
        ),
    ]
