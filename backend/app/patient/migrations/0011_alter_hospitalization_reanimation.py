# Generated by Django 4.2.13 on 2024-06-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0010_alter_hospitalization_reanimation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalization',
            name='reanimation',
            field=models.BooleanField(choices=[('reanimation', True), ('not_in_reanimation', False)], default=True),
        ),
    ]