class Hospital:
    def __init__(self):
        self.patient_count = 0

    def admit_patient(self):
        self.patient_count += 1

    def discharge_patient(self):
        if self.patient_count > 0:
            self.patient_count -= 1
        else:
            print("No patients to discharge.")

    def get_patient_count(self):
        return self.patient_count

# Example usage:
hospital = Hospital()

# Admit three patients
hospital.admit_patient()
hospital.admit_patient()
hospital.admit_patient()

print("Total number of patients:", hospital.get_patient_count())

# Discharge a patient
hospital.discharge_patient()

print("Total number of patients after discharge:", hospital.get_patient_count())

