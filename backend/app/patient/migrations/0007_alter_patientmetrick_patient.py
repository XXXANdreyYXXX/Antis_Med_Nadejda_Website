# Generated by Django 4.2.13 on 2024-06-11 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_patientmetrick_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmetrick',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]
