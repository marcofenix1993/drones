from django.db import models
from api.models import Drone, Medication


class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    # todo: update name to medication
    medications = models.ForeignKey(Medication, on_delete=models.CASCADE)

    def __str__(self):
        return "package"
