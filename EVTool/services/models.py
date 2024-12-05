from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Service(models.Model):
    AREA_CHOICES = [
        ('insurance', 'Insurance'),
        ('repair', 'Repair'),
        ('parts', 'Parts'),
        ('charging', 'Charging'),
        ('maintenance', 'Maintenance'),
        ('rent', 'Rent'),
        ('leasing', 'Leasing'),
        ('other', 'Other'),
    ]

    name = models.CharField(
        validators=[MinLengthValidator(3)],
        max_length=100,)
    text = models.CharField(
        validators=[MinLengthValidator(10)],
        max_length=1000,)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="services",)
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
    )
    area = models.CharField(
        max_length=50,
        choices=AREA_CHOICES,
        verbose_name="Service Area",
        default='other',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="When the service was created. Visible only to staff."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
        help_text="When the service was last updated. Visible only to staff."
    )

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save initially to generate ID

        if not self.slug:
            self.slug = slugify(f"{self.area}-{self.id}")
            super().save(*args, **kwargs)  # Save again to update slug with ID

    def __str__(self):
        return f"{self.name} ({self.area})"
