# Generated by Django 4.2.13 on 2024-06-09 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0003_alter_medcard_patient_metrick'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Diarie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bypass', models.CharField(blank=True, max_length=500, null=True)),
                ('examination', models.CharField(blank=True, max_length=500, null=True)),
                ('additional', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('diary_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_diary.diarytype')),
                ('med_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.medcard')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
