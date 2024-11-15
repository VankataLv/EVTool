from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models

from EVTool.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        unique=True,
        max_length=150,
    )
    email = models.EmailField(
        unique=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_business = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email',]

    objects = AppUserManager()