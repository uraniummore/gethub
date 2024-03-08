# Generated by Django 5.0.2 on 2024-03-08 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_management', '0002_remove_car_color_alter_car_vin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='MaintenanceTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('mileage_threshold', models.PositiveIntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_management.car')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_date', models.DateField()),
                ('elapsed_mileage', models.PositiveIntegerField()),
                ('notes', models.TextField(max_length=1000)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_management.maintenancetask')),
            ],
        ),
    ]
