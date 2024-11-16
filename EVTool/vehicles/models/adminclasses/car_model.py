from django.db import models

from EVTool.vehicles.models.adminclasses.brand import Brand, MODEL_BRAND_MAX_LENGTH


class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=MODEL_BRAND_MAX_LENGTH, unique=True)

    class Meta:
        unique_together = ('brand', 'name')

    def __str__(self):
        return f'{self.brand} - {self.name}'