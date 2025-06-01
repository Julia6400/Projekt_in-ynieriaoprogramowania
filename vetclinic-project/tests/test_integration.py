import unittest
from models.patient import Patient
from models.appointment import Appointment

class TestIntegration(unittest.TestCase):
    def test_patient_with_appointment(self):
        patient = Patient(1, "Reksio", "pies", "beagle", 4, "Anna Kowalska")
        appointment = Appointment(100, patient.patient_id, "Dr. Jan Nowak", "2025-06-05", "Szczepienie")

        self.assertEqual(appointment.patient_id, patient.patient_id)
        self.assertIn("Reksio", str(patient))
        self.assertIn("Szczepienie", str(appointment))
