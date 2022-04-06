# Generated by Django 4.0.1 on 2022-04-05 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_and_income', '0019_merge_20220405_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='dozen_eggs_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='half_dozen_eggs_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='single_egg_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='ten_eggs_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='trays_of_eggs_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]