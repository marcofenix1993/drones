from api.models import Medication


def get_medications_list():
    return list(Medication.objects.all())
