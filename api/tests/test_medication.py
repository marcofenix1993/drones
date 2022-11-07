from api.models import Medication
from django.core.exceptions import ValidationError
from django.test import TestCase


class MedicationTestCase(TestCase):

    def setUp(self):
        self.medication = Medication()
        self.medication.name = 'Tylenol'
        self.medication.weight = 20
        self.medication.code = "TYL25"
        self.medication.image_url = "medications/1.jpeg"

    def test_name(self):
        self.medication.full_clean()
        self.assertEqual(self.medication.name, 'Tylenol')
        with self.assertRaises(ValidationError) as e:
            self.medication.name = "Tylenol*02"
            self.medication.full_clean()
        self.assertEqual(e.exception.message_dict['name'][0],
                         "This field accepts only alphanumeric and  '-', '_' characters")

    def test_code(self):
        self.medication.full_clean()
        self.assertEqual(self.medication.code, 'TYL25')
        with self.assertRaises(ValidationError) as e:
            self.medication.code = "TYL25-"
            self.medication.full_clean()
        self.assertEqual(e.exception.message_dict['code'][0],
                         "This field accepts only uppercase letters, numbers and underscore characters")

