import unittest
from models.patient import Patient

class TestPatient(unittest.TestCase):
    def setUp(self):
        self.patient = Patient(1, "Reksio", "pies", "beagle", 4, "Anna Kowalska")

    def test_initialization(self):
        self.assertEqual(self.patient.name, "Reksio")
        self.assertEqual(self.patient.species, "pies")
        self.assertEqual(self.patient.breed, "beagle")
        self.assertEqual(self.patient.age, 4)
        self.assertEqual(self.patient.owner_name, "Anna Kowalska")

    def test_str_representation(self):
        expected = "Reksio (pies, beagle), 4 lat – Właściciel: Anna Kowalska"
        self.assertEqual(str(self.patient), expected)
