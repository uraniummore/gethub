import re

from django.core.exceptions import ValidationError


def validate_mileage(value):
    if not isinstance(value, int):
        raise ValidationError("Mileage should be an integer.", params={"value": value})

    if value <= 0:
        raise ValidationError("Mileage should be a positive integer.", params={"value": value})


def validate_alphanumeric_with_spaces(value):
    if not re.match(r'^[a-zA-Z0-9\s]+$', value):
        raise ValidationError('Only alphanumeric characters and spaces are allowed.')


def validate_vin(value):
    if not re.match(r'^[A-HJ-NPR-Z0-9]{17}$', value):
        raise ValidationError('Invalid VIN format.')
