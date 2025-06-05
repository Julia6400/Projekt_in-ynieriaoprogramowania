class Veterinarian:
    """
    Klasa reprezentująca lekarza weterynarii w gabinecie weterynaryjnym.
    """

    def __init__(self, first_name: str, last_name: str, specialization: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization

    def __str__(self) -> str:
        return f"Dr {self.first_name} {self.last_name} - {self.specialization}"

    def get_full_name(self) -> str:
        """
        Zwraca pełne imię i nazwisko lekarza.
        """
        return f"{self.first_name} {self.last_name}"

    def change_specialization(self, new_specialization: str) -> None:
        """
        Zmienia specjalizację lekarza.
        """
        self.specialization = new_specialization