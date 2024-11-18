from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from EVTool.vehicles.models.adminclasses.bike_model import BikeModel
from EVTool.vehicles.models.adminclasses.brand import Brand
from EVTool.vehicles.models.base_ev import BaseEV


class EVBike(BaseEV):
    BODY_TYPE_CHOICES = [
        ("ATV", "ATV"),
        ("Roadster", "Roadster"),
        ("Cross", "Cross"),
        ("Track", "Track"),
        ("Тricycle", "Тricycle"),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING,)
    model = models.ForeignKey(BikeModel, on_delete=models.DO_NOTHING,)

    mileage = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1_000_000),
        ],
        default=0,
    )

    body_type = models.CharField(
        max_length=15,
        choices=BODY_TYPE_CHOICES,
        default='unknown',
    )

    def __str__(self):
        return f'{self.year} - {self.color} - {self.brand.name}: {self.model.name}'
