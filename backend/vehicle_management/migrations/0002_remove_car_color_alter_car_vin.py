# Generated by Django 5.0.2 on 2024-03-07 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='color',
        ),
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(max_length=17, unique=True),
        ),
    ]
