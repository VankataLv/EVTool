from django.core.exceptions import ValidationError
from django.db import models


def validate_image_size(image):
    MAX_IMAGE_SIZE_MB = 5
    if image.size > MAX_IMAGE_SIZE_MB * 1024 * 1024:
        raise ValidationError("The image file size is too large. Please upload a smaller file.")


class EVCarPhoto(models.Model):
    image = models.ImageField(upload_to="photos/cars/", validators=[validate_image_size])
    description = models.CharField(max_length=255, blank=True,)
    car = models.ForeignKey(
        to='EVCar',
        on_delete=models.CASCADE,
        related_name='car_photos'
    )

    def __str__(self):
        return f"Photo of {self.car} - {self.description}"


class EVBikePhoto(models.Model):
    image = models.ImageField(upload_to="photos/bikes/", validators=[validate_image_size])
    description = models.CharField(max_length=255, blank=True,)
    bike = models.ForeignKey(
        to='EVBike',
        on_delete=models.CASCADE,
        related_name='bike_photos'
    )

    def __str__(self):
        return f"Photo of {self.bike} - {self.description}"
