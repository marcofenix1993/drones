import logging

from celery import shared_task

from api.models import Drone
from api.models.battery_level_history import BatteryLevelHistory

logger = logging.getLogger(__name__)


@shared_task()
def check_drones_battery_level():
    drones = Drone.objects.all()
    for drone in drones:
        battery_level_history = BatteryLevelHistory()
        battery_level_history.drone = drone
        battery_level_history.battery_level = drone.battery_capacity
        battery_level_history.save()
        logger.info(f'Drone: {drone.serial_number}. Battery Level: {drone.battery_capacity}')
