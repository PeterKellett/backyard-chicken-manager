# Generated by Django 4.0.1 on 2022-03-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EggCollectionSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('customer_name_eggs_collection', models.CharField(max_length=250)),
                ('normal_order_qty_eggs_collection', models.IntegerField(blank=True)),
                ('qty_sold_eggs_collection', models.IntegerField()),
                ('qty_given_free_eggs_collection', models.IntegerField(blank=True)),
                ('amount_paid_eggs_collection', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('balance_owed_eggs_collection', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('breakages_and_loses_eggs_collection', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EggDeliverySales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('customer_name_eggs_delivery', models.CharField(max_length=250)),
                ('normal_order_qty_eggs_delivery', models.IntegerField(blank=True)),
                ('delivery_due_date', models.DateTimeField()),
                ('delivery_not_made', models.BooleanField(blank=True)),
                ('delivery_not_made_reason', models.CharField(max_length=250)),
                ('qty_sold_eggs_delivery', models.IntegerField()),
                ('qty_given_free_eggs_delivery', models.IntegerField(blank=True)),
                ('amount_paid_eggs_delivery', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('balance_owed_eggs_delivery', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('breakages_and_loses_eggs_delivery', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EggMarketSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('venue_location_eggs_market', models.CharField(blank=True, max_length=250)),
                ('single_egg_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('half_dozen_eggs_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('ten_eggs_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('dozen_eggs_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('trays_of_eggs_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('qty_single_eggs_sold', models.IntegerField(blank=True)),
                ('qty_half_dozen_egg_boxes_sold', models.IntegerField(blank=True)),
                ('qty_ten_egg_boxes_sold', models.IntegerField(blank=True)),
                ('qty_dozen_egg_boxes_sold', models.IntegerField(blank=True)),
                ('qty_trays_of_eggs_sold', models.IntegerField(blank=True)),
                ('amount_paid_eggs_market', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('sales_amount_eggs_roadside', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('sales_paid_difference_eggs_roadside', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('loses_eggs_market', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EggRoadsideSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('single_egg_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('half_dozen_eggs_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('ten_eggs_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('dozen_eggs_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('trays_of_eggs_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('qty_single_eggs_remaining', models.IntegerField(blank=True)),
                ('qty_single_eggs_added', models.IntegerField(blank=True)),
                ('qty_half_dozen_egg_boxes_remaining', models.IntegerField(blank=True)),
                ('qty_half_dozen_egg_boxes_added', models.IntegerField(blank=True)),
                ('qty_ten_egg_boxes_remaining', models.IntegerField(blank=True)),
                ('qty_ten_egg_boxes_added', models.IntegerField(blank=True)),
                ('qty_dozen_egg_boxes_remaining', models.IntegerField(blank=True)),
                ('qty_dozen_egg_boxes_added', models.IntegerField(blank=True)),
                ('qty_trays_of_eggs_remaining', models.IntegerField(blank=True)),
                ('qty_trays_of_eggs_added', models.IntegerField(blank=True)),
                ('amount_paid_eggs_roadside', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('sales_amount_eggs_roadside', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('sales_paid_difference_eggs_roadside', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('loses_eggs_roadside', models.IntegerField(blank=True)),
            ],
        ),
    ]
