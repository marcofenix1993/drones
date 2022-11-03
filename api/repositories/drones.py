from django.db.models import Sum

from api.models import Drone, Package, Medication


def get_drones_list():
    return list(Drone.objects.all())


def get_drone_by_id(drone_id):
    return Drone.objects.get(pk=drone_id)


def new_drone(drone):
    return Drone.objects.create(drone)


def load_medications(drone_id, medications_ids):
    drone = Drone.objects.get(pk=drone_id)
    if not drone.can_load():
        raise Exception("The drone can't load the medication. Battery low.")
    current_weight = sum(
        [package.medications.weight for package in Package.objects.filter(active=True, drone_id=drone_id)])
    MedicationsQuery = Medication.objects.filter(pk__in=medications_ids)
    if not MedicationsQuery.exists():
        raise Exception("Invalid Medication")
    weight_to_load = MedicationsQuery.aggregate(Sum('weight')).get('weight__sum', 0)
    if current_weight + weight_to_load > drone.weight_limit:
        raise Exception("The weight to be loaded exceeds the weight limit of the drone")
    drone.state = "LOADING"
    for medication_id in medications_ids:
        medication = Medication.objects.get(pk=medication_id)
        new_package = Package()
        new_package.drone = drone
        new_package.medications = medication
        new_package.active = True
        new_package.save()


def drone_medications_list(drone_id):
    # todo: check that drone exist
    drone = get_drone_by_id(drone_id)
    packages = Package.objects.filter(active=True, drone_id=drone_id)
    medications = []
    for package in packages:
        medications.append(package.medications)
    return medications


def available_drones_list():
    return list(Drone.objects.filter(state='IDLE'))

