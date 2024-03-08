from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    vin = models.CharField(max_length=17, unique=True)

    def __repr__(self):
        return f"Car(title=\"{self.title}\")"

    def __str__(self):
        return self.title


class MaintenanceTask(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    mileage_threshold = models.PositiveIntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


class MaintenanceEntry(models.Model):
    maintenance_date = models.DateField()
    elapsed_mileage = models.PositiveIntegerField()
    notes = models.TextField(max_length=1000)
    task = models.ForeignKey(MaintenanceTask, on_delete=models.CASCADE)
