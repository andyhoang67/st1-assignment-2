class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def update_details(self):
        pass

    def view_appointments(self):
        pass


class Practitioner:
    def __init__(self, practitioner_id, name, availability):
        self.practitioner_id = practitioner_id
        self.name = name
        self.availability = availability

    def view_availability(self):
        pass

    def view_appointments(self):
        pass


class Appointment:
    def __init__(self, appointment_id, patient, practitioner,
                 date_time, status):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = status

    def create_appointment(self):
        pass

    def cancel_appointment(self):
        pass

    def update_status(self):
        pass