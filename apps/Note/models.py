from django.db import models

from apps.Place.models import Place
from utils.absmodel import AbstractBaseModel





class Folder(AbstractBaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    space=models.ForeignKey(Place,related_name='folders',on_delete=models.CASCADE)


class Note(AbstractBaseModel):
    name = models.CharField(max_length=100)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='notes',null=True)
    space = models.ForeignKey(Place, related_name='notes', on_delete=models.CASCADE)
    content = models.TextField()




