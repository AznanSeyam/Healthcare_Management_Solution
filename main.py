import patient
import doctor
import appointment
import billing

def main_menu():
        print("\nClinic Management System")
        print("1. Manage Patients")
        print("2. Manage Doctors")
        print("3. Schedule Appointments")
        print("4. Billing")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient.patient_menu()
        elif choice == "2":
            doctor.doctor_menu()
        elif choice == "3":
            appointment.appointment_menu()
        elif choice == "4":
            billing.billing_menu()
        elif choice == "5":
            print("Exiting Clinic Management System...")
            break
        else:
            print("Invalid choice! Please select again.")

if __name__ == "__main__":
    main_menu()
