# Generated by Django 4.0.1 on 2022-03-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_and_income', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EggDeliverySalesDashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('breakages_and_loses_eggs_delivery', models.IntegerField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='eggdeliverysales',
            name='breakages_and_loses_eggs_delivery',
        ),
    ]
