import database

def appointment_menu():
    while True:
        print("\nAppointment Management")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Cancel Appointment")
        print("4. Go Back")

        choice = input("Enter choice: ")

        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            cancel_appointment()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def book_appointment():
    appointment_id = input("Enter Appointment ID: ")
    patient_id = input("Enter Patient ID: ")
    doctor_id = input("Enter Doctor ID: ")
    date = input("Enter Date (YYYY-MM-DD): ")
    time = input("Enter Time (HH:MM): ")
    database.book_appointment(appointment_id, patient_id, doctor_id, date, time)

def view_appointments():
    appointments = database.get_appointments()
    for appointment in appointments:
        print(appointment)

def cancel_appointment():
    appointment_id = input("Enter Appointment ID to cancel: ")
    database.cancel_appointment(appointment_id)
