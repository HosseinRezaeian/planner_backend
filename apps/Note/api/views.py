from django.shortcuts import render
from rest_framework.filters import BaseFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status, viewsets

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from apps.Note.api.serializers.folder import FolderSerializer, FolderGetSerializer
from apps.Note.api.serializers.noteContent import NoteContentSerializer
from apps.Note.models import Note, Folder, NoteContent
from apps.Note.api.serializers.note import NoteSerializer
from apps.Note.queryset import PathParameterFolderAndSpaceFilterBackend, PathParameterSpaceFilterBackend, \
    PathParameterSpaceAndFolderAndNoteFilterBackend

@extend_schema(tags=['Note'])
class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [PathParameterFolderAndSpaceFilterBackend]


@extend_schema(tags=['Folder'])
class FolderViewSet(ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    filter_backends=[PathParameterSpaceFilterBackend]
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FolderGetSerializer
        return FolderSerializer



@extend_schema(tags=['Note Content'])
class NoteContentViewSet(viewsets.ModelViewSet):
    queryset = NoteContent.objects.all()
    serializer_class = NoteContentSerializer
    filter_backends = [PathParameterSpaceAndFolderAndNoteFilterBackend]

    @extend_schema(
        summary="Move item up",
        description="Moves the selected item one position up.",
        responses={200: {"description": "Item moved up"}}
    )
    @action(detail=True, methods=['post'])
    def move_up(self, request, pk=None):
        item = self.get_object()
        item.move_up()
        return Response({'status': 'item moved up'}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Move item down",
        description="Moves the selected item one position down.",
        responses={200: {"description": "Item moved down"}}
    )
    @action(detail=True, methods=['post'])
    def move_down(self, request, pk=None):
        item = self.get_object()
        item.move_down()
        return Response({'status': 'item moved down'}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Move item to top",
        description="Moves the selected item to the top position.",
        responses={200: {"description": "Item moved to top"}}
    )
    @action(detail=True, methods=['post'])
    def move_to_top(self, request, pk=None):
        item = self.get_object()
        item.move_to_top()
        return Response({'status': 'item moved to top'}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Move item to bottom",
        description="Moves the selected item to the bottom position.",
        responses={200: {"description": "Item moved to bottom"}}
    )
    @action(detail=True, methods=['post'])
    def move_to_bottom(self, request, pk=None):
        item = self.get_object()
        item.move_to_bottom()
        return Response({'status': 'item moved to bottom'}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Move item above another item",
        description="Moves the selected item above the specified target item.",
        parameters=[
            OpenApiParameter(
                name="target_item_id",
                description="ID of the target item above which the current item should be moved.",
                required=True,
                type=int
            )
        ],
        responses={
            200: {"description": "Item moved above target item"},
            400: {"description": "target_item_id is required"},
            404: {"description": "Target item not found"}
        }
    )
    @action(detail=True, methods=['post'])
    def move_above(self, request, pk=None):
        item = self.get_object()
        target_item_id = request.data.get('target_item_id')
        if not target_item_id:
            return Response({'error': 'target_item_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            target_item = NoteContent.objects.get(id=target_item_id)
            item.move_above(target_item)
            return Response({'status': f'item moved above {target_item.name}'}, status=status.HTTP_200_OK)
        except NoteContent.DoesNotExist:
            return Response({'error': 'target item not found'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        summary="Move item below another item",
        description="Moves the selected item below the specified target item.",
        parameters=[
            OpenApiParameter(
                name="target_item_id",
                description="ID of the target item below which the current item should be moved.",
                required=True,
                type=int
            )
        ],
        responses={
            200: {"description": "Item moved below target item"},
            400: {"description": "target_item_id is required"},
            404: {"description": "Target item not found"}
        }
    )
    @action(detail=True, methods=['post'])
    def move_below(self, request, pk=None):
        item = self.get_object()
        target_item_id = request.data.get('target_item_id')
        if not target_item_id:
            return Response({'error': 'target_item_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            target_item = NoteContent.objects.get(id=target_item_id)
            item.move_below(target_item)
            return Response({'status': f'item moved below {target_item.name}'}, status=status.HTTP_200_OK)
        except NoteContent.DoesNotExist:
            return Response({'error': 'target item not found'}, status=status.HTTP_404_NOT_FOUND)
