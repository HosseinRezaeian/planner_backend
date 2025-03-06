from apps.Place.models import Place


class CurrentUrlSpaceSerializerField:
    requires_context = True

    def __call__(self, serializer_field):
        space_id = serializer_field.context['view'].kwargs['space_key']
        obj = Place.objects.get(id=space_id)
        return obj

    def __repr__(self):
        return '%s()' % self.__class__.__name__