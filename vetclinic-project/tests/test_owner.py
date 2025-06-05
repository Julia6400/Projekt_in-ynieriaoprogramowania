import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from models.owner import Owner

class TestOwner(unittest.TestCase):
    """Testy jednostkowe dla klasy Owner."""

    def setUp(self):
        """Przygotowanie danych testowych przed każdym testem."""
        self.owner = Owner("Anna", "Kowalska", "123-456-789")

    def test_owner_creation(self):
        """Test tworzenia obiektu Owner z poprawnymi danymi."""
        self.assertEqual(self.owner.first_name, "Anna")
        self.assertEqual(self.owner.last_name, "Kowalska")
        self.assertEqual(self.owner.phone, "123-456-789")

    def test_owner_str_representation(self):
        """Test reprezentacji tekstowej obiektu Owner."""
        expected = "Anna Kowalska - tel: 123-456-789"
        self.assertEqual(str(self.owner), expected)

    def test_owner_methods(self):
        """Test metod get_full_name() i update_phone()."""
        # Test get_full_name()
        self.assertEqual(self.owner.get_full_name(), "Anna Kowalska")

        # Test update_phone()
        self.owner.update_phone("987-654-321")
        self.assertEqual(self.owner.phone, "987-654-321")
        self.assertEqual(str(self.owner), "Anna Kowalska - tel: 987-654-321")


if __name__ == "__main__":
    unittest.main()