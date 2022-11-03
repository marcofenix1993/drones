from django.db import models

from api.models import Drone


class BatteryLevelHistory(models.Model):
    date = models.DateTimeField(auto_now=True)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    battery_level = models.FloatField()
