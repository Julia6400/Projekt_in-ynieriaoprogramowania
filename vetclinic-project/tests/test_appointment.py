import unittest
from models.appointment import Appointment

class TestAppointment(unittest.TestCase):
    def setUp(self):
        self.appointment = Appointment(100, 1, "Dr. Jan Nowak", "2025-06-05", "Szczepienie")

    def test_initialization(self):
        self.assertEqual(self.appointment.appointment_id, 100)
        self.assertEqual(self.appointment.patient_id, 1)
        self.assertEqual(self.appointment.vet_name, "Dr. Jan Nowak")
        self.assertEqual(self.appointment.date, "2025-06-05")
        self.assertEqual(self.appointment.service, "Szczepienie")

    def test_str_representation(self):
        expected = "Wizyta 100: 2025-06-05 – Szczepienie u Dr. Jan Nowak (Pacjent ID: 1)"
        self.assertEqual(str(self.appointment), expected)
