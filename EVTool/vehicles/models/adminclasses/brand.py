from django.db import models

MODEL_BRAND_MAX_LENGTH = 50


class Brand(models.Model):
    name = models.CharField(max_length=MODEL_BRAND_MAX_LENGTH, unique=True)
    logo = models.ImageField(upload_to="brandlogos/")

    def __str__(self):
        return self.name
