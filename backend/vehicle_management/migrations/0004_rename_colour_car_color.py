# Generated by Django 5.0.2 on 2024-03-07 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_management', '0003_rename_color_car_colour'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='colour',
            new_name='color',
        ),
    ]
