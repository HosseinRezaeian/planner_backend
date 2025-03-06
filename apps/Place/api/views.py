from django.db import transaction
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.Account.api.serializers import AccountSpaceSerializer
from apps.Place.api.serializers import PlaceSerializer
from apps.Place.models import Place


# Create your views here.




class PlaceCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    def post(self, request, *args, **kwargs):
        user = request.user
        places = user.places.all()
        with transaction.atomic():
            new_place=Place.objects.create(creator=user,**request.data)
            new_place.users.set([user])
            new_place.save()
            return Response({"result":"success"})
