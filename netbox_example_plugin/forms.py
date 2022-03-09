from django import forms
from utilities.forms import (
    BootstrapMixin, BulkEditForm
)
from .models import Animal


class AnimalEditForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('name', 'sound')


class AnimalFilterForm(BootstrapMixin, forms.Form):
    model = Animal
    q = forms.CharField(
        required=False,
        label='Search'
    )


class AnimalBulkEditForm(BulkEditForm):
    name = forms.CharField(
        max_length=200,
        required=True
    )

    sound = forms.CharField(
        max_length=200,
        required=True
    )
