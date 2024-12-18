from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
