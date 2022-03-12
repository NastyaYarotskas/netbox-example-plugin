from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator, RegexValidator


def name_validator(name):
    if name == "moon":
        raise ValidationError("{} is not a valid animal name.".format(name))


AnimalNameValidator = RegexValidator(
    regex='^[A-Za-z]+$',
    message='Only characters are allowed in animals names',
    code='invalid'
)
