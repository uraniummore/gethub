# Generated by Django 5.0.2 on 2024-03-07 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_management', '0005_alter_car_mileage_alter_car_title_alter_car_vin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='color',
        ),
    ]
