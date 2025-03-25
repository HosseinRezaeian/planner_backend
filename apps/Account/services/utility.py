from apps.Note.models import Folder, Note
from apps.Place.models import Place


class CurrentUrlSpaceSerializerField:
    requires_context = True

    def __call__(self, serializer_field):
        space_id = serializer_field.context['view'].kwargs['space_key']
        obj = Place.objects.get(id=space_id)
        return obj

    def __repr__(self):
        return '%s()' % self.__class__.__name__


from rest_framework.exceptions import NotFound
from apps.Place.models import Place
from apps.Note.models import Folder

class CurrentUrlFolderSerializerField:
    requires_context = True

    def __call__(self, serializer_field):

        folder_id = serializer_field.context['view'].kwargs.get('folder')
        space_id = serializer_field.context['view'].kwargs.get('space_key')
        if not folder_id or not space_id:
            raise NotFound(detail="Both 'folder' and 'space_key' must be provided in the URL.", code=400)
        try:
            obj = Folder.objects.get(id=folder_id, space_id=space_id)
        except Folder.DoesNotExist:
            raise NotFound(detail=f"Folder with ID {folder_id} and Space ID {space_id} does not exist.", code=404)
        return obj

    def __repr__(self):
        return '%s()' % self.__class__.__name__



class CurrentUrlNoteSerializerField:
    requires_context = True

    def __call__(self, serializer_field):

        folder_id = serializer_field.context['view'].kwargs.get('folder')
        note = serializer_field.context['view'].kwargs.get('note')
        space_id = serializer_field.context['view'].kwargs.get('space_key')
        if not folder_id or not space_id or not note:
            raise NotFound(detail="Both 'folder' and 'space_key' must be provided in the URL.", code=400)
        try:
            obj = Note.objects.get(folder_id=folder_id, space_id=space_id,id=note)
        except Folder.DoesNotExist:
            raise NotFound(detail=f"Folder with ID {folder_id} and Space ID {space_id} does not exist.", code=404)
        return obj

    def __repr__(self):
        return '%s()' % self.__class__.__name__
