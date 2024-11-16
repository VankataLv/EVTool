from django.db import models


class Municipality(models.Model):
    municipality_name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = "Municipalities"

    def __str__(self):
        return self.municipality_name
