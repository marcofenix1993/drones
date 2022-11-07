from api.models import Drone
from django.db import models


class BatteryLevelHistory(models.Model):
    date = models.DateTimeField(auto_now=True)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    battery_level = models.FloatField()
