from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.timezone import now

from EVTool.vehicles.models.adminclasses.color import Color
from EVTool.vehicles.models.adminclasses.municipality import Municipality

UserModel = get_user_model()


def validate_year(value):
    current_year = now().year
    if value < 1900 or value > current_year:
        raise ValidationError(f'Year must be between 1900 and {current_year}.')


class BaseEV(models.Model):
    class Meta:
        abstract = True

    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE,)
    location = models.ForeignKey(Municipality, on_delete=models.DO_NOTHING,)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    asking_price = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1_000_000),
        ],
        help_text='Price in EUR. Only whole numbers',
    )
    battery_capacity = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text='In kWh. Up to two decimals',
    )
    range = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10_000),
        ],
        default=None,
        help_text='WLTP rating or other tool in km',
    )
    description = models.TextField(blank=True)
    horsepower = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1_000),
        ],
        default=0,
    )
    year = models.IntegerField(
        validators=[validate_year,],
        default=None,
    )
    vin = models.CharField(
        max_length=17,
        help_text="Vehicle Identification Number",
        unique=True,
        null=True,
        blank=True,
    )
