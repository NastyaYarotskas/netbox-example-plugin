from rest_framework.routers import APIRootView
from .. import filters
from ..models import Animal
from netbox.api.views import ModelViewSet
from . import serializers


class ExamplePluginRootView(APIRootView):
    """
    API root view
    """

    def get_view_name(self):
        return 'Animals'


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = serializers.AnimalSerializer
    filterset_class = filters.AnimalFilterSet
