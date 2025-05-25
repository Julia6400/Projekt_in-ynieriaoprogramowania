import unittest
from src.models.patient import Patient

# Test klasy patient
class TestPatient(unittest.TestCase):
    def test_patient_str(self):
        patient = Patient("Reksio", "pies", "beagle", 4, "Anna Kowalska")
        expected = "Reksio (pies, beagle), 4 lat – Właściciel: Anna Kowalska"
        self.assertEqual(str(patient), expected)

if __name__ == "__main__":
    unittest.main()
