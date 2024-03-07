from django.db import models


class Car(models.Model):
    def __repr__(self):
        return f"Car(title=\"{self.title}\")"

    def __str__(self):
        return self.title

    title = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    colour = models.CharField(max_length=100)
    mileage = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True)
