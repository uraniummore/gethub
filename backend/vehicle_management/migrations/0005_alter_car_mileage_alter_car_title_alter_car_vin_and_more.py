# Generated by Django 5.0.2 on 2024-03-07 18:58

import django.core.validators
import vehicle_management.validators.car_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_management', '0004_rename_colour_car_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(validators=[vehicle_management.validators.car_validator.validate_mileage]),
        ),
        migrations.AlterField(
            model_name='car',
            name='title',
            field=models.CharField(max_length=100, validators=[vehicle_management.validators.car_validator.validate_alphanumeric_with_spaces]),
        ),
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(max_length=17, unique=True, validators=[vehicle_management.validators.car_validator.validate_vin]),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1886, message='Year cannot be earlier than 1886.'), django.core.validators.MaxValueValidator(2024, message='Car cannot be manufactured in future yet.')]),
        ),
    ]