from rest_framework import serializers

from apps.Account.services.utility import CurrentUrlSpaceSerializerField
from apps.Note.api.serializers.note import NoteSerializer
# from apps.Account import serializers
from apps.Note.models import Folder
from apps.Place.models import Place
from utils.absserializers import AbstractSerializer
from rest_framework.generics import GenericAPIView




class FolderSerializer(AbstractSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    space=serializers.HiddenField(default=CurrentUrlSpaceSerializerField())

    class Meta:
        model = Folder
        fields = ['id','name','description','creator','space']


class FolderGetSerializer(AbstractSerializer):
    notes = NoteSerializer(many=True, read_only=True)
    class Meta:
        model = Folder
        fields = ['id','name','description','creator','notes','space']