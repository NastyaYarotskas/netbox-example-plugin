from django.db import models
from django.urls import reverse

from netbox.models import PrimaryModel
from utilities.querysets import RestrictedQuerySet
from extras.utils import extras_features

from netbox_example_plugin.validators import name_validator, AnimalNameValidator


@extras_features('custom_fields', 'custom_links', 'export_templates', 'tags', 'webhooks')
class Animal(PrimaryModel):
    name = models.CharField(max_length=64, validators=[name_validator, AnimalNameValidator])
    sound = models.CharField(max_length=64)

    objects = RestrictedQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('plugins:netbox_example_plugin:animal', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
