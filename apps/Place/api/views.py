from django.db import transaction
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.Account.api.serializers import AccountSpaceSerializer
from apps.Place.api.serializers import PlaceSerializer, PlaceListSerializer
from apps.Place.models import Place, PlaceUser


# Create your views here.




class PlaceCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    def post(self, request, *args, **kwargs):
        user = request.user
        # places = user.places.all()
        with transaction.atomic():
            new_place=Place.objects.create(creator=user,**request.data)
            new_place.users.set([user])
            new_place.save()
            return Response({"result":"success"})


class PlaceListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Place.objects.all()
    serializer_class = PlaceListSerializer
    def list(self, request, *args, **kwargs):
        user = request.user
        places = user.places.all()

        return Response(PlaceListSerializer(places, many=True,context={"user":user}).data)

class PlaceUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Place.objects.all()
    serializer_class = PlaceListSerializer


    def update(self, request, *args, **kwargs):
        try:
            user = request.user
            data = request.data.copy()
            place_id = kwargs['place_id']

            if not place_id:
                return Response({"result": "fail", "error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():
                if "select" in data:
                    select = data.pop("select")
                    if select:
                        PlaceUser.objects.filter(user=user).update(select=False)
                    PlaceUser.objects.filter(user=user, place__id=place_id).update(select=select)

                updated_rows = Place.objects.filter(id=place_id).update(**data)
                if updated_rows == 0 and data:
                    return Response({"result": "fail", "error": "Place not found"}, status=status.HTTP_404_NOT_FOUND)

            return Response({"result": "success"})

        except Exception as e:
            return Response({"result": "fail", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

