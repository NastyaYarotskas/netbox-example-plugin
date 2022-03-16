from django import forms
from utilities.forms import (
    BootstrapMixin, BulkEditForm, CSVModelForm
)
from .models import Animal
from .choices import AnimalStatusChoices


class AnimalEditForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('name', 'sound', 'status')


class AnimalFilterForm(BootstrapMixin, forms.Form):
    model = Animal
    q = forms.CharField(
        required=False,
        label='Search'
    )


class AnimalBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=Animal.objects.all(),
        widget=forms.MultipleHiddenInput
    )

    name = forms.CharField(
        max_length=200,
        required=True
    )

    sound = forms.CharField(
        max_length=200,
        required=True
    )

    status = forms.ChoiceField(
        choices=AnimalStatusChoices,
        required=False
    )

    class Meta:
        nullable_fields = []


class AnimalCSVForm(CSVModelForm):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'sound', 'status']
