import rest_framework.serializers as serializers

from apps.Place.models import Place, PlaceUser
from utils.absserializers import AbstractSerializer


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = ["name"]



class PlaceListSerializer(AbstractSerializer):
    select=serializers.SerializerMethodField()
    class Meta:
        model = Place
        fields = ["id","name","select"]

    def get_select(self, obj):
        user = self.context["user"]
        place_user = PlaceUser.objects.filter(user=user, place=obj).first()
        return place_user.select if place_user else False