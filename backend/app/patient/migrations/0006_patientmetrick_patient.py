# Generated by Django 4.2.13 on 2024-06-11 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_remove_medcard_patient_metrick_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmetrick',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
            preserve_default=False,
        ),
    ]