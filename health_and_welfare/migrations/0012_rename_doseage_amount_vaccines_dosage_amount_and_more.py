# Generated by Django 4.0.1 on 2022-05-16 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health_and_welfare', '0011_medicinesname_farm_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaccines',
            old_name='doseage_amount',
            new_name='dosage_amount',
        ),
        migrations.AddField(
            model_name='medicines',
            name='qty_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vaccines',
            name='dose_per_bird',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vaccines',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='vaccines',
            name='vaccine_name',
            field=models.CharField(default='vaccine', max_length=50),
            preserve_default=False,
        ),
    ]