from django.urls import path
from api.views import drones_list, medications_list, add_medications_to_drone, medications_by_drone, available_drones, \
    drone_battery_level, battery_level_history

urlpatterns = [
    path('drones', drones_list),
    path('drones/<str:drone_id>/medications', medications_by_drone),
    path('drones/<str:drone_id>/add_medications', add_medications_to_drone),
    path('drones/<str:drone_id>/battery_level', drone_battery_level),
    path('drones/availables', available_drones),
    path('drones/battery_level_history', battery_level_history),
    path('medications', medications_list)
]
