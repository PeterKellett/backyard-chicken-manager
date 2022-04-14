# Generated by Django 4.0.1 on 2022-04-12 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flock_management', '0005_rename_farm_id_coops_farm_profile_and_more'),
        ('profiles', '0009_alter_userprofile_city_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Purchases Category',
            },
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('product', models.CharField(blank=True, max_length=50, null=True)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('amount_purchased', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('unit_of_measurement', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=50, null=True)),
                ('receipt_reference', models.CharField(blank=True, max_length=50, null=True)),
                ('seller_name', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenditure.purchasescategory')),
                ('farm_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.farmprofile')),
                ('flock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flock_management.flocks')),
            ],
            options={
                'verbose_name_plural': 'Purchases',
            },
        ),
    ]
