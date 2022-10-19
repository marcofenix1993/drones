import json
from django.core import serializers
from django.http import JsonResponse
from api.repositories.drones import get_drones_list
from api.repositories.medications import get_medications_list


def drones_list(request):
    drones_set = get_drones_list()
    data = serializers.serialize('json', drones_set, fields=('serial_number', 'medal', 'weight_limit', 'battery_capacity', 'state'))
    return JsonResponse(json.loads(data), safe=False)


def medications_list(request):
    medications_set = get_medications_list()
    data = serializers.serialize('json', medications_set,
                                 fields=('name', 'code', 'weight', 'image_url'))
    return JsonResponse(json.loads(data), safe=False)
