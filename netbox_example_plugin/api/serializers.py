from netbox.api.serializers import PrimaryModelSerializer
from ..models import Animal


class AnimalSerializer(PrimaryModelSerializer):
    class Meta:
        model = Animal
        fields = [
            "id", "name", "sound",
        ]
