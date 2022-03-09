from rest_framework import serializers
from netbox.api.serializers import PrimaryModelSerializer
from ..models import Animal


class AnimalSerializer(PrimaryModelSerializer):
    name = serializers.CharField(read_only=True)
    sound = serializers.CharField(read_only=True)

    class Meta:
        model = Animal
        fields = [
            "id", "name", "sound",
        ]
