# Generated by Django 4.0.1 on 2022-02-18 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_farmprofile_user'),
        ('flock_management', '0002_alter_flocks_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flocks',
            name='farm_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flocks', to='profiles.farmprofile'),
        ),
    ]
