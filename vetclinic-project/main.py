from src.models.patient import Patient
from src.models.appointment import Appointment

def main():
    # Tworzymy pacjenta
    patient = Patient(
        patient_id=1,
        name="Reksio",
        species="pies",
        breed="beagle",
        age=4,
        owner_name="Anna Kowalska"
    )

    # Tworzymy wizytę dla tego pacjenta
    appointment = Appointment(
        appointment_id=100,
        patient_id=patient.patient_id,
        vet_name="Dr. Jan Nowak",
        date="2025-06-05",
        service="Szczepienie"
    )

    # Wyświetlamy informacje
    print("=== Pacjent ===")
    print(patient)

    print("\n=== Wizyta ===")
    print(appointment)

if __name__ == "__main__":
    main()
