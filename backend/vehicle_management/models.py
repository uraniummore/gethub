from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True)

    def __repr__(self):
        return f"Car(title=\"{self.title}\")"

    def __str__(self):
        return self.title
