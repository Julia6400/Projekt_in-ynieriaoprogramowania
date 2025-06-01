import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.patient import Patient
import unittest

class TestPatient(unittest.TestCase):
    def test_patient_initialization(self):
        patient = Patient("Reksio", "pies", "beagle", 4, "Anna Kowalska")
        self.assertEqual(patient.name, "Reksio")

    def test_patient_str(self):
        patient = Patient("Reksio", "pies", "beagle", 4, "Anna Kowalska")
        expected = "Reksio (pies, beagle), 4 lat – Właściciel: Anna Kowalska"
        self.assertEqual(str(patient), expected)

if __name__ == "__main__":
    unittest.main()
