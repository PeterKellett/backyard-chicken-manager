# Generated by Django 4.0.1 on 2022-05-18 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_userprofile_city_country'),
        ('health_and_welfare', '0014_vaccinesname_farm_profile_virusesname_farm_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplementsname',
            name='farm_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.farmprofile'),
        ),
    ]
