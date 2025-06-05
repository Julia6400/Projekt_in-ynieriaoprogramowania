import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.veterinarian import Veterinarian

class TestVeterinarian(unittest.TestCase):
    """Testy jednostkowe dla klasy Veterinarian."""

    def setUp(self):
        """Przygotowanie danych testowych przed każdym testem."""
        self.vet = Veterinarian("Jan", "Nowak", "chirurgia")

    def test_veterinarian_creation(self):
        """Test tworzenia obiektu Veterinarian z poprawnymi danymi."""
        self.assertEqual(self.vet.first_name, "Jan")
        self.assertEqual(self.vet.last_name, "Nowak")
        self.assertEqual(self.vet.specialization, "chirurgia")

    def test_veterinarian_str_representation(self):
        """Test reprezentacji tekstowej obiektu Veterinarian."""
        expected = "Dr Jan Nowak - chirurgia"
        self.assertEqual(str(self.vet), expected)

    def test_veterinarian_methods(self):
        """Test metod get_full_name() i change_specialization()."""
        # Test get_full_name()
        self.assertEqual(self.vet.get_full_name(), "Jan Nowak")

        # Test change_specialization()
        self.vet.change_specialization("kardiologia")
        self.assertEqual(self.vet.specialization, "kardiologia")
        self.assertEqual(str(self.vet), "Dr Jan Nowak - kardiologia")


if __name__ == "__main__":
    unittest.main()