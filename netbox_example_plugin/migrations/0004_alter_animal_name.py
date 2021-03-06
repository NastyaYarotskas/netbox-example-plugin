# Generated by Django 3.2.12 on 2022-03-12 11:47

import django.core.validators
from django.db import migrations, models
import netbox_example_plugin.validators


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_example_plugin', '0003_alter_animal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='name',
            field=models.CharField(max_length=64, validators=[netbox_example_plugin.validators.name_validator, django.core.validators.RegexValidator(code='invalid', message='Only characters are allowed in animals names', regex='^[A-Za-z]+$')]),
        ),
    ]
