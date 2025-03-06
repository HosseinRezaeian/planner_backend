from django.db import models

from django.contrib.auth import get_user_model
from utils.absmodel import AbstractBaseModel


class Place(AbstractBaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    users = models.ManyToManyField(get_user_model(), related_name='places')