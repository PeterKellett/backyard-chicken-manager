# Generated by Django 4.0.1 on 2022-04-20 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regular_tasks', '0026_feedingtime_amount_water_consumed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedingtime',
            name='food_total',
        ),
    ]