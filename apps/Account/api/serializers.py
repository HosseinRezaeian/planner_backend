from rest_framework import serializers

from apps.Account.models import User
from apps.Place.models import Place
from utils.absserializers import AbstractSerializer


class AccountGetSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=("username","email")

class AccountSpaceSerializer(AbstractSerializer):

    class Meta:
        model=Place
        fields=("id","name")

