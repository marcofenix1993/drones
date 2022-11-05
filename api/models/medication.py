import re

from django.core.exceptions import ValidationError
from django.db import models

ModelType = models.TextChoices('ModelType', 'Lightweight Middleweight Cruiserweight Heavyweight')
StateType = models.TextChoices('StateType', 'IDLE LOADING LOADED DELIVERING DELIVERED RETURNING')


def validate_name(value):
    if re.match(r'^[A-Za-z0-9_-]+$', value):
        return value
    raise ValidationError("This field accepts only alphanumeric and  '-', '_' characters")


def validate_code(value):
    if re.match(r'^[A-Z0-9_]+$', value):
        return value
    raise ValidationError("This field accepts only uppercase letters, numbers and underscore characters")


class Medication(models.Model):
    name = models.CharField(max_length=100, null=False, validators=[validate_name])
    code = models.CharField(max_length=100, null=False, primary_key=True, validators=[validate_code])
    weight = models.IntegerField()
    image_url = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
