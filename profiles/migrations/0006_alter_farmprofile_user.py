# Generated by Django 4.0.1 on 2022-02-18 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_farmprofile_sales_units_dozen_carton_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farmprofiles', to='profiles.userprofile'),
        ),
    ]