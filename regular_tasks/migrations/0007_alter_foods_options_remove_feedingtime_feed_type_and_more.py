# Generated by Django 4.0.1 on 2022-03-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regular_tasks', '0006_eggcollection_farm_profile_eggcollection_flock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foods',
            options={'verbose_name_plural': 'Foods'},
        ),
        migrations.RemoveField(
            model_name='feedingtime',
            name='feed_type',
        ),
        migrations.AlterField(
            model_name='feedingtime',
            name='amount_food_added',
            field=models.IntegerField(verbose_name='amount of food added'),
        ),
        migrations.AlterField(
            model_name='feedingtime',
            name='amount_food_rem',
            field=models.IntegerField(verbose_name='amount of food remaining'),
        ),
        migrations.AlterField(
            model_name='feedingtime',
            name='amount_water_added',
            field=models.IntegerField(verbose_name='amount of water added'),
        ),
        migrations.AlterField(
            model_name='feedingtime',
            name='amount_water_rem',
            field=models.IntegerField(verbose_name='amount of water remaining'),
        ),
        migrations.AlterField(
            model_name='feedingtime',
            name='date',
            field=models.DateTimeField(verbose_name='date'),
        ),
    ]
