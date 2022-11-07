import json
import random
import string

from api.models import Drone, Medication, Package
from django.core.exceptions import ValidationError
from django.db import DataError
from django.test import Client, TestCase


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


class DroneTestCase(TestCase):
    fixtures = ['api/fixtures/medications.json', 'api/tests/fixtures/test_drone.json']

    def setUp(self):
        self.invalid_serial_number = get_random_string(101)
        self.drone = Drone()
        self.drone.serial_number = "ae25"
        self.drone.weight_limit = 50
        self.drone.battery_capacity = 1
        self.drone.state = "IDLE"

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

    def test_weight_limit_exceeded(self):
        c = Client()
        self.drone.full_clean()
        self.drone.save()
        medication = Medication.objects.get(pk="YUOPTFSN")
        new_package = Package()
        new_package.drone = self.drone
        new_package.medications = medication
        new_package.active = True
        new_package.save()
        post_data = ["KNKNJK"]
        response = c.post(f'/api/drones/{self.drone.serial_number}/add_medications', json.dumps(post_data), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.json(), {'error': 'The weight to be loaded exceeds the weight limit of the drone'})

    def test_battery_low_prevent_loading(self):
        self.drone.battery_capacity = 0.24
        self.drone.state = "LOADING"
        self.assertEqual(self.drone.can_load(), False)

    def test_drone_limit(self):
        c = Client()
        post_data = {
            "serial_number": "def45",
            "model": "Lightweight",
            "weight_limit": 500,
            "battery_capacity": 1,
            "state": "IDLE"
        }
        response = c.post('/api/drones', json.dumps(post_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        post_data = {
            "serial_number": "def53",
            "model": "Lightweight",
            "weight_limit": 500,
            "battery_capacity": 1,
            "state": "IDLE"
        }
        response = c.post('/api/drones', json.dumps(post_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.json(),
                             {'error': 'Maximum amount of drones allowed is 10'})
