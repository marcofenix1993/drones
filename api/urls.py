from django.urls import path
from api.views import drones_list, medications_list

urlpatterns = [
    path('drones/', drones_list),
    path('medications/', medications_list)
]
