# Generated by Django 4.2.13 on 2024-06-15 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0014_alter_hospitalization_reanimation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientmetrick',
            old_name='puls',
            new_name='pulse',
        ),
    ]
