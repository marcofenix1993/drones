from django.contrib import admin
from django.contrib.admin import ModelAdmin

from api.models import Drone, Medication


@admin.register(Drone)
class DroneAdmin(ModelAdmin):
    pass


@admin.register(Medication)
class MedicationAdmin(ModelAdmin):
    pass
