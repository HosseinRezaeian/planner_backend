from django.db import models
from ordered_model.models import OrderedModel

from apps.Place.models import Place
from utils.absmodel import AbstractBaseModel


class Folder(AbstractBaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(default="", null=True, blank=True)
    space = models.ForeignKey(Place, related_name='folders', on_delete=models.CASCADE)


class Note(AbstractBaseModel):
    name = models.CharField(max_length=100)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='notes', null=True)
    space = models.ForeignKey(Place, related_name='notes', on_delete=models.CASCADE)



class NoteContent(AbstractBaseModel,OrderedModel):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='content')
    space = models.ForeignKey(Place, related_name='place_note_contents', on_delete=models.CASCADE)


    class FiledName(models.TextChoices):
        Markdown = "md"
        Text = "text"
        Checkbox = "checkbox"
    is_checked = models.BooleanField(default=False)
    filed_type = models.CharField(max_length=100, choices=FiledName.choices, default=FiledName.Text)
    content = models.TextField(default="", blank=True, null=True)

