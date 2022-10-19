import json
from django.core import serializers
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden

from api.models import Drone
from api.repositories.drones import get_drones_list, load_medications, drone_medications_list
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
        drone.save()
        data = serializers.serialize('json', [drone],
                                     fields=('serial_number', 'medal', 'weight_limit', 'battery_capacity', 'state'))
        return JsonResponse(json.loads(data), safe=False, status=201)
    return HttpResponseForbidden()


def add_medications_to_drone(request, drone_id):
    if request.method == 'POST':
        medications_ids = json.loads(request.body)
        load_medications(drone_id, medications_ids)
        return HttpResponse("done", status=200)
    return HttpResponseForbidden()


def medications_by_drone(request, drone_id):
    if request.method == 'GET':
        medications = drone_medications_list(drone_id)
        data = serializers.serialize('json', medications,
                                     fields=('name', 'code', 'weight', 'image_url'))
        return JsonResponse(json.loads(data), safe=False)
    return HttpResponseForbidden()


def medications_list(request):
    if request.method == 'GET':
        medications_set = get_medications_list()
        data = serializers.serialize('json', medications_set,
                                     fields=('name', 'code', 'weight', 'image_url'))
        return JsonResponse(json.loads(data), safe=False)
    return HttpResponseForbidden()
