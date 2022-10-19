from django.db import models
from api.models.drone import Drone
from api.models.medication import Medication


class Package(models.Model):
    id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    medications = models.ForeignKey(Medication, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
