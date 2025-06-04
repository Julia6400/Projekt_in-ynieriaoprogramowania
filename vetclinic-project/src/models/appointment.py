class Appointment:
    """
    Klasa reprezentująca wizytę w klinice weterynaryjnej.
    """

    def __init__(self, appointment_id: int, patient_id: int, vet_name: str, date: str, service: str) -> None:
        """
        Inicjalizuje nową wizytę.

        :param appointment_id: unikalny identyfikator wizyty
        :param patient_id: identyfikator pacjenta
        :param vet_name: imię i nazwisko weterynarza
        :param date: data wizyty w formacie 'YYYY-MM-DD'
        :param service: opis usługi (np. szczepienie, badanie kontrolne)
        """
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.vet_name = vet_name
        self.date = date
        self.service = service

    def __str__(self) -> str:
        return f"Wizyta {self.appointment_id}: {self.date} – {self.service} u {self.vet_name} (Pacjent ID: {self.patient_id})"
