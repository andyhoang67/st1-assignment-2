SCHEDULED = "Scheduled"
CANCELLED = "Cancelled"


class Patient:
    def __init__(self, patient_id, name):
        self.__patient_id = patient_id
        self.__name = name

    def set_patient_id(self, patient_id):
        if patient_id != "":
            self.__patient_id = patient_id
        else:
            print("Invalid patient ID.")

    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Invalid patient name.")

    def get_patient_id(self):
        return self.__patient_id

    def get_name(self):
        return self.__name


class Practitioner:
    def __init__(self, practitioner_id, name, specialty):
        self.__practitioner_id = practitioner_id
        self.__name = name
        self.__specialty = specialty

    def get_practitioner_id(self):
        return self.__practitioner_id

    def get_name(self):
        return self.__name

    def get_specialty(self):
        return self.__specialty


class Appointment:
    def __init__(self, appointment_id, patient, practitioner, date_time):
        self.__appointment_id = appointment_id
        self.__patient = patient
        self.__practitioner = practitioner
        self.__date_time = date_time
        self.__status = SCHEDULED

    def get_appointment_id(self):
        return self.__appointment_id

    def get_status(self):
        return self.__status

    def cancel_appointment(self):
        if self.__status == SCHEDULED:
            self.__status = CANCELLED
            print("Appointment cancelled.")
        else:
            print("Invalid transition. Appointment is already cancelled.")


patient1 = Patient("P001", "Alex Smith")

practitioner1 = Practitioner(
    "PR001",
    "Dr Sarah Lee",
    "General Practice"
)

appointment1 = Appointment(
    "A001",
    patient1,
    practitioner1,
    "25/09/2026 10:30 AM"
)

print("Test 1 - Valid objects")
print("Patient:", patient1.get_name())
print("Practitioner:", practitioner1.get_name())
print("Appointment ID:", appointment1.get_appointment_id())
print("Status:", appointment1.get_status())



print("\nTest 2 - Invalid input")

patient1.set_name("")

print("Patient name:", patient1.get_name())



print("\nTest 3 - Cancel appointment")

appointment1.cancel_appointment()

print("Status:", appointment1.get_status())


print("\nTest 4 - Cancel again")

appointment1.cancel_appointment()

print("Status:", appointment1.get_status())