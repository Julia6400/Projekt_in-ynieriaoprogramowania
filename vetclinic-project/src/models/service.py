class Service:
    """
    Klasa reprezentująca usługi świadczone przez klinikę weterynaryjną.

    Atrybuty:
    service_id (int): Unikalny identyfikator usługi.
    name (str): Nazwa usługi (np. szczepienie przeciwko wściekliźnie).
    category (str): Kategoria usługi (np. diagnostyka, profilaktyka).
    species (str): Gatunek zwierzęcia, dla którego przeznaczona jest usługa.
    price (float): Cena usługi w złotówkach.

    """

    def __init__(self, service_id: int, name: str, category: str, species: str, price: float) -> None:

        self.service_id = service_id
        self.name = name
        self.category = category
        self.species = species
        self.price = price


    def __str__(self) -> str:
        return f"{self.service_id} ({self.name}, {self.category}, {self.species}) – koszt: {self.price:.2f} zł"

