import json
from django.core import serializers
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden

from api.models import Drone
from api.repositories.battery_level_history import battery_level_history_list
from api.repositories.drones import get_drones_list, load_medications, drone_medications_list, available_drones_list, \
    get_drone_by_id
from api.repositories.medications import get_medications_list


def drones_list(request):
    if request.method == 'GET':
        drones_set = get_drones_list()
        data = serializers.serialize('json', drones_set,
                                     fields=('serial_number', 'model', 'weight_limit', 'battery_capacity', 'state'))
        return JsonResponse(json.loads(data), safe=False)
    elif request.method == 'POST':
        drone = Drone()
        drone.from_json(json.loads(request.body))
        if not drone.is_valid():
            return JsonResponse({
                "error": "Battery low, the drone can't be in loading state",
            }, status=400)
        try:
            drone.full_clean()
            drone.save()
        except ValidationError as e:
            return JsonResponse({"errors": e.message_dict}, safe=False, status=400)
        data = serializers.serialize('json', [drone],
                                     fields=('serial_number', 'medal', 'weight_limit', 'battery_capacity', 'state'))
        return JsonResponse(json.loads(data), safe=False, status=201)
    return HttpResponseForbidden()


def add_medications_to_drone(request, drone_id):
    if request.method == 'POST':
        medications_ids = json.loads(request.body)
        try:
            load_medications(drone_id, medications_ids)
            return HttpResponse("done", status=200)
        except Exception as e:
            return JsonResponse({
                "error": e.args[0],
            }, status=400)
    return HttpResponseForbidden()


def medications_by_drone(request, drone_id):
    if request.method == 'GET':
        try:
            medications = drone_medications_list(drone_id)
            data = serializers.serialize('json', medications,
                                         fields=('name', 'code', 'weight', 'image_url'))
            return JsonResponse(json.loads(data), safe=False)
        except Drone.DoesNotExist as e:
            return JsonResponse({
                "error": e.args[0],
            }, status=404)
    return HttpResponseForbidden()


def medications_list(request):
    if request.method == 'GET':
        medications_set = get_medications_list()
        data = serializers.serialize('json', medications_set,
                                     fields=('name', 'code', 'weight', 'image_url'))
        return JsonResponse(json.loads(data), safe=False)
    return HttpResponseForbidden()


def available_drones(request):
    if request.method == 'GET':
        drones = available_drones_list()
        data = serializers.serialize('json', drones,
                                     fields=('serial_number', 'medal', 'weight_limit', 'battery_capacity', 'state'))
        return JsonResponse(json.loads(data), safe=False)
    return HttpResponseForbidden()


def battery_level_history(request):
    if request.method == 'GET':
        history_list = battery_level_history_list()
        data = serializers.serialize('json', history_list,
                                     fields=('drone', 'date', 'battery_level'))
        return JsonResponse(json.loads(data), safe=False)
    return HttpResponseForbidden()


def drone_battery_level(request, drone_id):
    if request.method == 'GET':
        try:
            drone = get_drone_by_id(drone_id)
        except Drone.DoesNotExist as e:
            return JsonResponse({
                "error": e.args[0],
            }, status=404)
        data = serializers.serialize('json', [drone],
                                     fields=('battery_capacity'))
        return JsonResponse(json.loads(data), safe=False)
    return HttpResponseForbidden()
