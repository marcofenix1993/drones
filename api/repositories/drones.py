from api.models import Drone


def get_drones_list():
    return list(Drone.objects.all())


def new_drone(drone):
    return Drone.objects.create(drone)
