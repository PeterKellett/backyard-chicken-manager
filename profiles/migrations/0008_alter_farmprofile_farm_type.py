# Generated by Django 4.0.1 on 2022-02-28 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_rename_user_farmprofile_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmprofile',
            name='farm_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='farmtype', to='profiles.farmtype'),
        ),
    ]
