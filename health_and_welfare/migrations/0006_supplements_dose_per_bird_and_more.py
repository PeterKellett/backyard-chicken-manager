# Generated by Django 4.0.1 on 2022-05-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_and_welfare', '0005_remove_supplements_qty_supplements_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplements',
            name='dose_per_bird',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='supplements',
            name='dosage_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
