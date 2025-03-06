from django.contrib.auth import get_user_model
from django.db import models
from hashid_field import HashidAutoField



class AbstractHashModel(models.Model):
    id = HashidAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('id',)


class AbstractBaseModel( models.Model):
    id = HashidAutoField(primary_key=True)
    creator = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('id',)


class AbstractWithoutCreatorBaseModel( models.Model):
    id = HashidAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('id',)


