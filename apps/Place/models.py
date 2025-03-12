from django.db import models

from django.contrib.auth import get_user_model
from utils.absmodel import AbstractBaseModel

class PlaceUser(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    place = models.ForeignKey("Place", on_delete=models.CASCADE)
    select = models.BooleanField(default=False)


class Place(AbstractBaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    users = models.ManyToManyField(
        get_user_model(),
        through=PlaceUser,
        related_name="places")