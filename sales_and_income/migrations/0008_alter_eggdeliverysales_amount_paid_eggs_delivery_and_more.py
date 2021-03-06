# Generated by Django 4.0.1 on 2022-03-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_and_income', '0007_remove_eggroadsidesales_farm_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggdeliverysales',
            name='amount_paid_eggs_delivery',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='eggdeliverysales',
            name='balance_owed_eggs_delivery',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='eggdeliverysales',
            name='customer_name_eggs_delivery',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='eggdeliverysales',
            name='delivery_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eggdeliverysales',
            name='delivery_not_made',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eggdeliverysales',
            name='delivery_not_made_reason',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='eggdeliverysales',
            name='normal_order_qty_eggs_delivery',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eggdeliverysales',
            name='qty_given_free_eggs_delivery',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eggdeliverysales',
            name='qty_sold_eggs_delivery',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
