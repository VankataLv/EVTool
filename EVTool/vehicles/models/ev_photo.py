from django.core.exceptions import ValidationError
from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


def validate_image_size(image):
    MAX_IMAGE_SIZE_MB = 5
    if image.size > MAX_IMAGE_SIZE_MB * 1024 * 1024:
        raise ValidationError("The image file size is too large. Please upload a smaller file.")


class EVPhoto(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    # THIS IS MANY-ONE-FIELD
    # generates model type field, for id(table_pk) 15 -> content_type is evcarphoto,
    # for if id(table_pk) 16 -> content_type is evcarbike,
    # object_id stores the id of the object that the photo is attached to;

    content_object = GenericForeignKey('content_type', 'object_id')

    image = models.ImageField(
        upload_to='ev_photos/',
        validators=[validate_image_size]
    )
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Photo for {self.content_object} - ({self.description})"
