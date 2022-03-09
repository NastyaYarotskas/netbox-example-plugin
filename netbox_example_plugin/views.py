from netbox.views import generic

from .models import Animal
from . import tables
from . import forms
from . import filters


class ListAnimalsView(generic.ObjectListView):
    """
    List all animals in the database.
    """
    queryset = Animal.objects.all()
    filterset = filters.AnimalFilterSet
    filterset_form = forms.AnimalFilterForm
    table = tables.AnimalTable
    template_name = 'netbox_example_plugin/animal_list.html'


class AnimalView(generic.ObjectView):
    """
    Display a single animal, identified by name in the URL.
    """
    queryset = Animal.objects.all()
    template_name = 'netbox_example_plugin/animal.html'


class AnimalEditView(generic.ObjectEditView):
    queryset = Animal.objects.all()
    model_form = forms.AnimalEditForm
    template_name = 'netbox_example_plugin/add_animal.html'


class AnimalBulkEditView(generic.BulkEditView):
    queryset = Animal.objects.all()
    filterset = filters.AnimalFilterSet
    table = tables.AnimalTable
    form = forms.AnimalBulkEditForm


class AnimalBulkDeleteView(generic.BulkDeleteView):
    queryset = Animal.objects.filter()
    filterset = filters.AnimalFilterSet
    table = tables.AnimalTable
    default_return_url = "plugins:netbox_example_plugin:animal_list"
