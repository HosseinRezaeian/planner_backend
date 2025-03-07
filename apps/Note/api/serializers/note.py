from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField

# from apps.Account import serializers
from apps.Note.models import Note,Folder
from utils.absserializers import AbstractSerializer


class NoteSerializer(AbstractSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    folder = serializers.PrimaryKeyRelatedField(
         queryset=Folder.objects.all(),pk_field=HashidSerializerCharField() )

    class Meta:
        model = Note
        fields = '__all__'



