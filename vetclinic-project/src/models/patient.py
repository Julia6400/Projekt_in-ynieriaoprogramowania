class Patient:
    """
    Klasa reprezentująca pacjenta w klinice weterynaryjnej.
    """

    def __init__(self, patient_id: int, name: str, species: str, breed: str, age: int, owner_name: str) -> None:
        """
        Inicjalizuje nowego pacjenta.

        :param patient_id: unikalny identyfikator pacjenta
        :param name: imię zwierzęcia
        :param species: gatunek (np. pies, kot)
        :param breed: rasa
        :param age: wiek w latach
        :param owner_name: imię i nazwisko właściciela
        """
        self.patient_id = patient_id
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.owner_name = owner_name

    def __str__(self) -> str:
        return f"{self.name} ({self.species}, {self.breed}), {self.age} lat – Właściciel: {self.owner_name}"
