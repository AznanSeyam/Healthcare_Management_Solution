patients = []
doctors = []
appointments = []
bills = []

def add_patient(patient_id, name, age, gender, disease):
    patients.append({"id": patient_id, "name": name, "age": age, "gender": gender, "disease": disease})




def add_doctor(doctor_id, name, specialty):
    doctors.append({"id": doctor_id, "name": name, "specialty": specialty})

def get_doctors():
    return doctors

def update_doctor(doctor_id, name, specialty):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            doctor.update({"name": name, "specialty": specialty})

def delete_doctor(doctor_id):
    global doctors
    doctors = [d for d in doctors if d["id"] != doctor_id]

def book_appointment(appointment_id, patient_id, doctor_id, date, time):
    appointments.append({"id": appointment_id, "patient_id": patient_id, "doctor_id": doctor_id, "date": date, "time": time})

def get_appointments():
    return appointments

def cancel_appointment(appointment_id):
    global appointments
    appointments = [a for a in appointments if a["id"] != appointment_id]

def add_bill(bill_id, patient_id, amount):
    bills.append({"id": bill_id, "patient_id": patient_id, "amount": amount})

def get_bills():
    return bills
