from .. import filters
from ..models import Animal
from rest_framework.viewsets import ModelViewSet
from . import serializers


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = serializers.AnimalSerializer
    filterset_class = filters.AnimalFilterSet
