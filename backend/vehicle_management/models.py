from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from vehicle_management.validators import car_validator


class Car(models.Model):
    title = models.CharField(max_length=100, validators=[car_validator.validate_alphanumeric_with_spaces])
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(
        validators=[
            MinValueValidator(1886, message="Year cannot be earlier than 1886."),
            MaxValueValidator(timezone.now().year, message="Car cannot be manufactured in future yet.")
        ]
    )
    color = models.CharField(max_length=100)
    mileage = models.IntegerField(validators=[car_validator.validate_mileage])
    vin = models.CharField(max_length=17, unique=True, validators=[car_validator.validate_vin])

    def __repr__(self):
        return f"Car(title=\"{self.title}\")"

    def __str__(self):
        return self.title
