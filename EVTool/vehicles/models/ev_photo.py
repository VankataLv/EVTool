from django.core.exceptions import ValidationError
from django.db import models
from EVTool.vehicles.models import EVCar, EVBike


def validate_image_size(image):
    MAX_IMAGE_SIZE_MB = 5
    if image.size > MAX_IMAGE_SIZE_MB * 1024 * 1024:
        raise ValidationError("The image file size is too large. Please upload a smaller file.")


class EvCarPhoto(models.Model):
    car = models.ForeignKey(EVCar, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='evcar_photos/',
                              validators=[validate_image_size,],)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Photo for {self.car} - ({self.description})"


class EvBikePhoto(models.Model):
    bike = models.ForeignKey(EVBike, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='evbike_photos/',
                              validators=[validate_image_size, ], )
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Photo for {self.bike} - ({self.description})"
