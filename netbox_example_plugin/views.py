from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import transaction

from netbox.views import generic

from .models import Animal
from . import tables
from . import forms
from . import filters
from .choices import AnimalStatusChoices


class ListAnimalsView(generic.ObjectListView):
    """
    List all animals in the database.
    """
    queryset = Animal.objects.all()
    filterset = filters.AnimalFilterSet
    filterset_form = forms.AnimalFilterForm
    table = tables.AnimalTable
    action_buttons = ()
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
    # template_name = 'netbox_example_plugin/add_animal.html'
    default_return_url = 'plugins:netbox_example_plugin:animal_list'


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


class AnimalDeleteView(generic.ObjectDeleteView):
    queryset = Animal.objects.all()


class AnimalBulkImportView(generic.BulkImportView):
    queryset = Animal.objects.filter()
    model_form = forms.AnimalCSVForm
    table = tables.AnimalTable


def free_animals(request):
    selected_objects = Animal.objects.all().filter(pk__in=request.POST.getlist('pk'))
    with transaction.atomic():
        for obj in selected_objects:
            obj.status = AnimalStatusChoices.STATUS_FREE
            obj.save()
    return HttpResponseRedirect(reverse('plugins:netbox_example_plugin:animal_list'))


def busy_animals(request):
    selected_objects = Animal.objects.all().filter(pk__in=request.POST.getlist('pk'))
    with transaction.atomic():
        for obj in selected_objects:
            obj.status = AnimalStatusChoices.STATUS_BUSY
            obj.save()
    return HttpResponseRedirect(reverse('plugins:netbox_example_plugin:animal_list'))
