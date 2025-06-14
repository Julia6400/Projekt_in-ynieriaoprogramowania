from datetime import date
from typing import List
from .service import Service

class Treatment:
    """
    Klasa reprezentująca leczenie danego zwierzaka.

    Atrybuty:
        treatment_date (date): Data leczenia.
        cost (float): Całkowity koszt leczenia.
        services (List[Service]): Lista wykonanych usług.
        description (str): Opis leczenia.
    """

    def __init__(self, treatment_date: date, services: List[Service], description: str) -> None:
        self.treatment_date = treatment_date
        self.services = services
        self.description = description
        self.cost = sum(service.price for service in services)

    def add_service(self, service: Service) -> None:
        """
        Dodaje usługę do leczenia i aktualizuje koszt.
        """
        self.services.append(service)
        self.cost += service.price

    def __str__(self) -> str:
        service_names = ', '.join([service.name for service in self.services])
        return (f"Leczenie z dnia {self.treatment_date}: {self.description} | "
                f"Usługi: {service_names} | Koszt całkowity: {self.cost:.2f} zł")
