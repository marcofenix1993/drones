from django.urls import path
from api.views import drones_list, medications_list, add_medications_to_drone, medications_by_drone

urlpatterns = [
    path('drones', drones_list),
    path('drones/<str:drone_id>/medications', medications_by_drone),
    path('drones/<str:drone_id>/add_medications', add_medications_to_drone),
    path('medications', medications_list)
]
