from rest_framework.filters import BaseFilterBackend


class PathParameterSpaceFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        space_id = view.kwargs['space_key']

        return queryset.filter(space=space_id)


from rest_framework.exceptions import NotFound

from rest_framework.exceptions import NotFound
from apps.Note.models import Folder

class PathParameterFolderAndSpaceFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        folder = view.kwargs.get('folder')
        space_id = view.kwargs.get('space_key')

        if not folder or not space_id:
            raise NotFound(detail="Folder or Space key is missing in the URL.", code=400)

        try:
            folder_obj = Folder.objects.get(id=folder)  # Ensure folder exists
        except Folder.DoesNotExist:
            raise NotFound(detail=f"Folder with ID {folder} does not exist.", code=404)

        return queryset.filter(folder=folder_obj, space=space_id)


class PathParameterSpaceAndFolderAndNoteFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        # folder = view.kwargs.get('folder')
        note = view.kwargs.get('note')
        space_id = view.kwargs.get('space_key')

        return queryset.filter(space=space_id,note=note)