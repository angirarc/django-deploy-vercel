# Generated by Django 5.1.7 on 2025-03-26 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_dailylog_createdon_alter_trip_createdon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailylog',
            name='driving_time',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='total_driving_time',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
