from django.db import models

ModelType = models.TextChoices('ModelType', 'Lightweight Middleweight Cruiserweight Heavyweight')
StateType = models.TextChoices('StateType', 'IDLE LOADING LOADED DELIVERING DELIVERED RETURNING')


class Drone(models.Model):
    serial_number = models.CharField(max_length=100, default='', null=False)
    medal = models.CharField(blank=True, choices=ModelType.choices, max_length=100)
    weight_limit = models.IntegerField()
    battery_capacity = models.FloatField()
    state = models.CharField(blank=True, choices=StateType.choices, max_length=100)

    def __str__(self):
        return self.serial_number
