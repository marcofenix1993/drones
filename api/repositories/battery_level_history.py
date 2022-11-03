from api.models.battery_level_history import BatteryLevelHistory


def battery_level_history_list():
    return list(BatteryLevelHistory.objects.all())
