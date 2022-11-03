import random
import string

from django.core.exceptions import ValidationError
from django.db import DataError
from django.test import TestCase

from api.models import Drone


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


class DroneTestCase(TestCase):

    def setUp(self):
        self.invalid_serial_number = get_random_string(101)

    def test_serial_number(self):
        with self.assertRaises(DataError):
            Drone.objects.create(serial_number=self.invalid_serial_number)

