class Patient:
    """
    Klasa reprezentująca pacjenta w gabinecie weterynaryjnym.
    """

    def __init__(self, name: str, species: str, breed: str, age: int, owner_name: str) -> None:
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.owner_name = owner_name

    def __str__(self) -> str:
        return f"{self.name} ({self.species}, {self.breed}), {self.age} lat – Właściciel: {self.owner_name}"
