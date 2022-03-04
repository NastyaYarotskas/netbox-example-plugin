from netbox.views import generic

from .models import Animal
from . import tables
from . import forms
from . import filters


class AnimalView(generic.ObjectView):
    """
    Display a single animal, identified by name in the URL.
    """
    queryset = Animal.objects.all()
    template_name = 'netbox_example_plugin/animal.html'


class ListAnimalsView(generic.ObjectListView):
    """
    List all animals in the database.
    """
    queryset = Animal.objects.all()
    filterset = filters.AnimalFilterSet
    filterset_form = forms.AnimalFilterForm
    table = tables.AnimalTable
    template_name = 'netbox_example_plugin/animal_list.html'


class AnimalEditView(generic.ObjectEditView):
    queryset = Animal.objects.all()
    model_form = forms.AnimalEditForm
    template_name = 'netbox_example_plugin/add_animal.html'
