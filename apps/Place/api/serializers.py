import rest_framework.serializers as serializers

from apps.Place.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ["name"]