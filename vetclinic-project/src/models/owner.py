class Owner:
    """
    Klasa reprezentująca właściciela zwierzęcia w gabinecie weterynaryjnym.
    """

    def __init__(self, first_name: str, last_name: str, phone: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - tel: {self.phone}"

    def get_full_name(self) -> str:
        """
        Zwraca pełne imię i nazwisko właściciela.
        """
        return f"{self.first_name} {self.last_name}"

    def update_phone(self, new_phone: str) -> None:
        """
        Aktualizuje numer telefonu właściciela.
        """
        self.phone = new_phone