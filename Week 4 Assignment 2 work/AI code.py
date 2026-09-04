def create_appointment():

    patient_name = input("Enter patient name: ")

    practitioner_name = input("Enter practitioner name: ")

    appointment_time = input("Enter appointment time: ")


    appointment = {

"patient": patient_name,

"practitioner": practitioner_name,

"time": appointment_time

}

    return appointment

# Create an appointment

appointment1 = create_appointment()


# Display the appointment

print("\nAppointment Details")

print(f"Patient: {appointment1['patient']}")

print(f"Practitioner: {appointment1['practitioner']}")

print(f"Time: {appointment1['time']}")