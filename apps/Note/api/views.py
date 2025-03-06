from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from apps.Note.api.serializers.folder import FolderSerializer, FolderGetSerializer
from apps.Note.models import Note, Folder
from apps.Note.api.serializers.note import NoteSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    def get_queryset(self):
        space_key = self.kwargs.get('space_key')
        return Note.objects.filter(space=space_key)


class FolderViewSet(ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FolderGetSerializer
        return FolderSerializer
    def get_queryset(self):
        space_key = self.kwargs.get('space_key')
        return Folder.objects.filter(space=space_key)
