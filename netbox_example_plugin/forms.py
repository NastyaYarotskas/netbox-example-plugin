from django import forms
from utilities.forms import (
    BootstrapMixin
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
