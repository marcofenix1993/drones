from django.db import models

ModelType = models.TextChoices('ModelType', 'Lightweight Middleweight Cruiserweight Heavyweight')
StateType = models.TextChoices('StateType', 'IDLE LOADING LOADED DELIVERING DELIVERED RETURNING')


class Drone(models.Model):
    serial_number = models.CharField(max_length=100, default='', null=False, primary_key=True)
    model = models.CharField(blank=True, choices=ModelType.choices, max_length=100)
    weight_limit = models.IntegerField()
    battery_capacity = models.FloatField()
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
