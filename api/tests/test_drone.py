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
        self.drone = Drone()
        self.drone.serial_number = "ae25"
        self.drone.weight_limit = 500

    def test_serial_number(self):
        with self.assertRaises(DataError):
            Drone.objects.create(serial_number=self.invalid_serial_number, model='Lightweight', weight_limit=490,
                                 state='IDLE')

    def test_weight_limit(self):
        with self.assertRaises(ValidationError) as e:
            self.drone.weight_limit = 505
            self.drone.battery_capacity = 1
            self.drone.full_clean()
            self.drone.save()
        self.assertEqual(e.exception.message_dict['weight_limit'][0], 'Weight value must be in range [0-500]')

    def test_battery_capacity(self):
        with self.assertRaises(ValidationError) as e:
            self.drone.battery_capacity = 5
            self.drone.full_clean()
            self.drone.save()
        self.assertEqual(e.exception.message_dict['battery_capacity'][0],
                         'Battery capacity value must be between 0 and 1')
