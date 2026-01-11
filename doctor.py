import database

def doctor_menu():
    while True:
        print("\nDoctor Management")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Update Doctor")
        print("4. Delete Doctor")
        print("5. Go Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_doctor()
        elif choice == "2":
            view_doctors()
        elif choice == "3":
            update_doctor()
        elif choice == "4":
            delete_doctor()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

def add_doctor():
    doctor_id = input("Enter Doctor ID: ")
    name = input("Enter Name: ")
    specialty = input("Enter Specialty: ")
    database.add_doctor(doctor_id, name, specialty)

def view_doctors():
    doctors = database.get_doctors()
    for doctor in doctors:
        print(doctor)

def update_doctor():
    doctor_id = input("Enter Doctor ID to update: ")
    name = input("Enter new Name: ")
    specialty = input("Enter new Specialty: ")
    database.update_doctor(doctor_id, name, specialty)

def delete_doctor():
    doctor_id = input("Enter Doctor ID to delete: ")
    database.delete_doctor(doctor_id)
