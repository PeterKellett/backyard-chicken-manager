# Generated by Django 4.0.1 on 2022-04-18 14:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flock_management', '0005_rename_farm_id_coops_farm_profile_and_more'),
        ('profiles', '0009_alter_userprofile_city_country'),
        ('health_and_welfare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrationMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administration_method', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Administration Methods',
            },
        ),
        migrations.CreateModel(
            name='DiseasesName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Disease Names',
            },
        ),
        migrations.CreateModel(
            name='MedicinesName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Medicine Names',
            },
        ),
        migrations.CreateModel(
            name='VaccinesName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Vaccine Names',
            },
        ),
        migrations.CreateModel(
            name='VirusesName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('virus_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Virus Names',
            },
        ),
        migrations.RemoveField(
            model_name='supplements',
            name='qty_supplement',
        ),
        migrations.AddField(
            model_name='supplements',
            name='qty_supplements',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='supplements',
            name='supplement_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Vaccines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('vaccine_name', models.CharField(blank=True, max_length=50, null=True)),
                ('virus_protected_against', models.CharField(blank=True, max_length=50, null=True)),
                ('qty_hens', models.IntegerField(blank=True, null=True)),
                ('qty_chicks', models.IntegerField(blank=True, null=True)),
                ('qty_cocks', models.IntegerField(blank=True, null=True)),
                ('qty_total', models.IntegerField(blank=True, null=True)),
                ('doseage_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('vet_administered', models.BooleanField(default=False)),
                ('vet_name', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('administration_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='health_and_welfare.administrationmethod')),
                ('farm_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.farmprofile')),
                ('flock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flock_management.flocks')),
            ],
        ),
        migrations.CreateModel(
            name='SupplementsName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplement_name', models.CharField(blank=True, max_length=50, null=True)),
                ('supplement_in_stock', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('farm_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.farmprofile')),
            ],
            options={
                'verbose_name_plural': 'Supplement Names',
            },
        ),
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('medicine_name', models.CharField(blank=True, max_length=50, null=True)),
                ('disease_protected_against', models.CharField(blank=True, max_length=50, null=True)),
                ('qty_hens', models.IntegerField(blank=True, null=True)),
                ('qty_chicks', models.IntegerField(blank=True, null=True)),
                ('qty_cocks', models.IntegerField(blank=True, null=True)),
                ('qty_total', models.IntegerField(blank=True, null=True)),
                ('doseage_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('vet_administered', models.BooleanField(default=False)),
                ('vet_name', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('administration_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_and_welfare.administrationmethod')),
                ('farm_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.farmprofile')),
                ('flock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='flock_management.flocks')),
            ],
            options={
                'verbose_name_plural': 'Medicines',
            },
        ),
    ]