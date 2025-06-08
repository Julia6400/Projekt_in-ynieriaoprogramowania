import unittest
from models.service import Service

class TestService(unittest.TestCase):

    def test_service_creation(self):
        service = Service(
            service_id = 1,
            name = "Szczepienie przeciwko wściekliźnie",
            category = "Profilaktyka",
            species = "Pies",
            price = 90.00)

        self.assertEqual(service.service_id, 1)
        self.assertEqual(service.name, "Szczepienie przeciwko wściekliźnie")
        self.assertEqual(service.category, "Profilaktyka")
        self.assertEqual(service.species, "Pies")
        self.assertEqual(service.price, 90.00)

    def test_service_str(self):
        service = Service(2, "Badanie", "Diagnostyka", "Kot", 150.5)
        expected = "2 (Badanie, Diagnostyka, Kot) – koszt: 150.50 zł"
        self.assertEqual(str(service), expected)

if __name__ == "__main__":
    unittest.main()