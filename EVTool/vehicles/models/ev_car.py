from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from EVTool.vehicles.models.adminclasses.car_model import CarModel
from EVTool.vehicles.models.base_ev import BaseEV
from EVTool.vehicles.models.adminclasses.brand import Brand


class EVCar(BaseEV):
    DRIVETRAIN_CHOICES = [
        ("fwd", "Front-wheel drive"),
        ("rwd", "Rear-wheel drive"),
        ("awd", "All-wheel drive"),
    ]

    BODY_TYPE_CHOICES = [
        ("sedan", "Sedan"),
        ("hatch", "Hatchback"),
        ("station_wagon", "Station wagon"),
        ("coupe", "Coupe"),
        ("suv", "SUV"),
        ("pickup_truck", "Pickup Truck"),
        ("minivan", "Minivan"),
        ("cabriolet", "Cabriolet"),
    ]

    DOORS_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, )
    model = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING,)
    trim_level = models.CharField(max_length=50, default='unknown')

    mileage = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1_000_000),
        ],
        default=0,
    )

    drivetrain = models.CharField(
        max_length=15,
        choices=DRIVETRAIN_CHOICES,
        default='unknown',
    )
    body_type = models.CharField(
        max_length=15,
        choices=BODY_TYPE_CHOICES,
        default='unknown',
    )

    doors = models.IntegerField(
        choices=DOORS_CHOICES,
        default=4,
    )

    def __str__(self):
        return f'{self.year} - {self.color} - {self.brand.name}: {self.model.name}'
