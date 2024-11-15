from django.contrib.auth import get_user_model
from django.db import models

from EVTool.accounts.models.validators import name_validator, nickname_validator, phone_number_validator

UserModel = get_user_model()


class Profile(models.Model):
    MAX_LENGTH_NAMES = 50

    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    nickname = models.CharField(
        unique=True,
        blank=True,
        null=True,
        max_length=MAX_LENGTH_NAMES,
        validators=[nickname_validator, ]
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        unique=True,
        blank=True,
        null=True,
        validators=[name_validator,]
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        unique=True,
        blank=True,
        null=True,
        validators=[name_validator,]
    )

    date_of_birth = models.DateField(
        unique=True,
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        unique=True,
        blank=True,
        null=True,
        max_length=12,
        validators=[phone_number_validator,]
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}".strip()

        return (self.first_name or self.last_name or self.user.email).strip()
