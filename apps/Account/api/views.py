from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.Account.models import User
from .serializers import AccountGetSerializer, AccountSpaceSerializer
from ...Place.models import Place


# Create your views here.
@extend_schema(
    summary="Retrieve a single account",
    description="Fetch details of a user by their ID",
    responses={200: AccountGetSerializer}
)



class AccountViewSet(generics.GenericAPIView, RetrieveModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = AccountGetSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        places=user.places.all()
        places=AccountSpaceSerializer(places, many=True).data

        data = {
            "email": user.email,
            "username": user.username,
            "places": places,
        }
        return Response(data)

