import django_filters
from django.db.models import Q
from netbox.filtersets import BaseFilterSet
from . import models


class AnimalFilterSet(BaseFilterSet):

    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )

    number = django_filters.ModelMultipleChoiceFilter(
        field_name='name',
        queryset=models.Animal.objects.all(),
        to_field_name='name',
        label='name',
    )

    class Meta():
        model = models.Animal
        fields = ('name',)

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value)
        )
