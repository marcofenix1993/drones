from api.models import Drone, Package, Medication


def get_drones_list():
    return list(Drone.objects.all())


def new_drone(drone):
    return Drone.objects.create(drone)


def load_medications(drone_id, medications_ids):
    # todo: check that the medications ids exist in the db
    # todo: check that the drone id is valid
    # todo: check that the medication didn't exceeded the limit of weight in the drone
    drone = Drone.objects.get(pk=drone_id)
    for medication_id in medications_ids:
        medication = Medication.objects.get(pk=medication_id)
        new_package = Package()
        new_package.drone = drone
        new_package.medications = medication
        new_package.active = True
        new_package.save()


def drone_medications_list(drone_id):
    # todo: check that drone exist
    drone = Drone.objects.get(pk=drone_id)
    packages = Package.objects.filter(active=True, drone_id=drone_id)
    medications = []
    for package in packages:
        medications.append(package.medications)
    return medications
