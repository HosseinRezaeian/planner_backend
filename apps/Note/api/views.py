from django.shortcuts import render
from rest_framework.filters import BaseFilterBackend

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


class PathParameterSpaceAndHrWorkingBoardObjetsFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        space_id = view.kwargs['space_key']

        return queryset.filter(space=space_id)
class FolderViewSet(ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    filter_backends=[PathParameterSpaceAndHrWorkingBoardObjetsFilterBackend]
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FolderGetSerializer
        return FolderSerializer
