# Generated by Django 4.2.13 on 2024-06-11 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_remove_medcard_additional_patient_metrick_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medcard',
            name='patient_metrick',
        ),
        migrations.RemoveField(
            model_name='patientmetrick',
            name='patient',
        ),
        migrations.AddField(
            model_name='hospitalization',
            name='ward',
            field=models.CharField(default='7', max_length=10),
        ),
        migrations.AddField(
            model_name='patientmetrick',
            name='med_card',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patient.medcard'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hospitalization',
            name='med_card_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.medcard'),
        ),
        migrations.AlterField(
            model_name='medcard',
            name='med_card_number',
            field=models.CharField(max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='patientmetrick',
            name='saturation',
            field=models.CharField(max_length=4),
        ),
    ]
