# Generated by Django 4.0.1 on 2022-03-24 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_and_income', '0009_remove_eggcollectionsales_customer_name_eggs_collection_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eggmarketsales',
            old_name='sales_amount_eggs_roadside',
            new_name='sales_amount_eggs_market',
        ),
        migrations.RenameField(
            model_name='eggmarketsales',
            old_name='sales_paid_difference_eggs_roadside',
            new_name='sales_paid_difference_eggs_market',
        ),
    ]
