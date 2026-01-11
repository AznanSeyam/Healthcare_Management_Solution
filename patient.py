import database

def patient_menu():
    while True:
        print("\nPatient Management")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Go Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            update_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")
    database.add_patient(patient_id, name, age, gender, disease)

def view_patients():
    patients = database.get_patients()
    for patient in patients:
        print(patient)

def update_patient():
    patient_id = input("Enter Patient ID to update: ")
    name = input("Enter new Name: ")
    age = input("Enter new Age: ")
    gender = input("Enter new Gender: ")
    disease = input("Enter new Disease: ")
    database.update_patient(patient_id, name, age, gender, disease)

def delete_patient():
    patient_id = input("Enter Patient ID to delete: ")
    database.delete_patient(patient_id)
