# Generated by Django 4.2.13 on 2024-06-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients_analysis', '0003_analysisindicator_indicator_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisindicator',
            name='indicator_norm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='analysisindicator',
            name='indicator_unit',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]