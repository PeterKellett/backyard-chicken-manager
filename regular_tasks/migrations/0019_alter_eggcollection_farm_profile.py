# Generated by Django 4.0.1 on 2022-03-21 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_userprofile_city_country'),
        ('regular_tasks', '0018_coopcleaning_images_eggcollection_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggcollection',
            name='farm_profile',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='profiles.farmprofile'),
            preserve_default=False,
        ),
    ]
