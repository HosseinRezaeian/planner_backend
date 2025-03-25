from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField

from apps.Account.services.utility import CurrentUrlSpaceSerializerField, CurrentUrlFolderSerializerField
from apps.Note.api.serializers.noteContent import NoteContentSerializer
# from apps.Account import serializers
from apps.Note.models import Note,Folder
from utils.absserializers import AbstractSerializer


class NoteSerializer(AbstractSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    folder = serializers.HiddenField(default=CurrentUrlFolderSerializerField())
    space = serializers.HiddenField(default=CurrentUrlSpaceSerializerField())
    content=NoteContentSerializer(many=True,required=False)
    class Meta:
        model = Note
        fields = ["id","name","folder","space","content","creator","created_at"]

    # def validate(self, attrs):
    #     folder = attrs["folder"]
    #     space = attrs["space"]
    #     if Folder.objects.filter(space=space,id=folder).exists():
    #         raise serializers.ValidationError('You are not a member of this space.')
    #     return attrs
# class NoteCreateSerializer(AbstractSerializer):
#     creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     folder = serializers.HiddenField(default=CurrentUrlFolderSerializerField())
#     space = serializers.HiddenField(default=CurrentUrlSpaceSerializerField())
#
#     content=NoteContentSerializer(many=True)
#     class Meta:
#         model = Note
#         fields = ["id","name","folder","space","content","creator","created_at"]