from django.core.exceptions import ValidationError
from django.db import models

ModelType = models.TextChoices('ModelType', 'Lightweight Middleweight Cruiserweight Heavyweight')
StateType = models.TextChoices('StateType', 'IDLE LOADING LOADED DELIVERING DELIVERED RETURNING')


def validate_weight_limit(value):
    if value < 0 or value > 500:
        raise ValidationError("Weight value must be in range [0-500]")
    return value


def validate_battery_capacity(value):
    if value < 0 or value > 1:
        raise ValidationError("Battery capacity value must be between 0 and 1")


class Drone(models.Model):
    serial_number = models.CharField(max_length=100, default='', null=False, primary_key=True)
    model = models.CharField(blank=True, choices=ModelType.choices, max_length=100)
    weight_limit = models.IntegerField(validators=[validate_weight_limit])
    battery_capacity = models.FloatField(validators=[validate_battery_capacity])
    state = models.CharField(blank=True, choices=StateType.choices, max_length=100)

    def __str__(self):
        return self.serial_number

    def from_json(self, fields):
        self.serial_number = fields['serial_number']
        self.model = fields['model']
        self.weight_limit = fields['weight_limit']
        self.battery_capacity = fields['battery_capacity']
        self.state = fields['state']

    def can_load(self):
        return self.battery_capacity >= 0.25 and self.state == 'IDLE'

    def is_valid(self):
        if self.state == 'LOADING' and self.battery_capacity < 0.25:
            return False
        return True
