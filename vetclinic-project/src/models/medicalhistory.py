class MedicalHistory:
    """
    Klasa reprezentująca historię medyczną pacjenta.
    """

    def __init__(self, patient: object) -> None:
        """
        Inicjalizuje historię medyczną dla danego pacjenta.

        :param patient: obiekt klasy Patient
        """
        self.patient = patient
        self.owner = patient.owner_name
        self.records = []
        self.list_treatment = set()

    def add_record(self, date: str, diagnosis: str, treatment: str, veterinarian: str, notes: str = "") -> None:
        """
        Dodaje nowy wpis do historii medycznej.

        :param date: data wizyty
        :param diagnosis: diagnoza pacjenta
        :param treatment: zastosowane leczenie
        :param veterinarian: imię i nazwisko lekarza weterynarii
        :param notes: dodatkowe uwagi
        """
        record = {
            "date": date,
            "diagnosis": diagnosis,
            "treatment": treatment,
            "veterinarian": veterinarian,
            "notes": notes
        }
        self.records.append(record)
        self.list_treatment.add(treatment)

    def get_all_records(self) -> list:
        """
        Zwraca wszystkie wpisy historii medycznej.

        :return: lista wpisów
        """
        return self.records

    def get_latest_record(self) -> dict | None:
        """
        Zwraca ostatni wpis, jeśli istnieje.

        :return: słownik z wpisem lub None
        """
        if self.records:
            return self.records[-1]
        return None

    def __str__(self) -> str:
        """
        Zwraca opis historii medycznej.

        :return: string z informacją o pacjencie i liczbie wpisów
        """
        return (
            f"Historia medyczna: {self.patient.name} ({self.patient.species}) – "
            f"{len(self.records)} wpisów, właściciel: {self.owner}"
