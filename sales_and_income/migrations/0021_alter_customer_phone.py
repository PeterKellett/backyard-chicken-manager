# Generated by Django 4.0.1 on 2022-04-06 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_and_income', '0020_customer_customer_sales_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
