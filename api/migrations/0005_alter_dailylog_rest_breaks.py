# Generated by Django 5.1.7 on 2025-03-26 20:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_trip_total_driving_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailylog',
            name='rest_breaks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None),
        ),
    ]
