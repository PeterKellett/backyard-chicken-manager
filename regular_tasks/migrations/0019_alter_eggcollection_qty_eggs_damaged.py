# Generated by Django 4.0.1 on 2022-03-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regular_tasks', '0018_alter_eggcollection_farm_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggcollection',
            name='qty_eggs_damaged',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]