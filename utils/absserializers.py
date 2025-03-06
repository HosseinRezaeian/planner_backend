from hashid_field.rest import HashidSerializerCharField
from rest_framework import serializers


class AbstractSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(read_only=True)

    class Meta:
        abstract = True
