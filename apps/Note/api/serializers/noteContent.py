from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField

from apps.Account.services.utility import CurrentUrlSpaceSerializerField, CurrentUrlNoteSerializerField
# from apps.Account import serializers
from apps.Note.models import Note, Folder, NoteContent
from utils.absserializers import AbstractSerializer


class NoteContentSerializer(AbstractSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    space = serializers.HiddenField(default=CurrentUrlSpaceSerializerField())
    note=serializers.HiddenField(default=CurrentUrlNoteSerializerField())

    class Meta:
        model = NoteContent
        fields = ["id", "space","note", "creator", "filed_type", "is_checked", "content", "order"]
