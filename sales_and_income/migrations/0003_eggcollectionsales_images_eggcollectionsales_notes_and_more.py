# Generated by Django 4.0.1 on 2022-03-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_and_income', '0002_eggdeliverysalesdashboard_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eggcollectionsales',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='eggcollectionsales',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eggdeliverysales',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='eggdeliverysales',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eggmarketsales',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='eggmarketsales',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eggroadsidesales',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='eggroadsidesales',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eggcollectionsales',
            name='customer_name_eggs_collection',
            field=models.CharField(default='', max_length=250),
        ),
    ]