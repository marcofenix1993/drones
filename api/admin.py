from django.contrib import admin
from django.contrib.admin import ModelAdmin

from api.models import Drone, Medication
from api.models.battery_level_history import BatteryLevelHistory


@admin.register(Drone)
class DroneAdmin(ModelAdmin):
    pass


@admin.register(Medication)
class MedicationAdmin(ModelAdmin):
    pass


@admin.register(BatteryLevelHistory)
class BatteryLevelHistoryAdmin(ModelAdmin):
    pass
