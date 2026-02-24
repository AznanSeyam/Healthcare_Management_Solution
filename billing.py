import database

def billing_menu():
    while True:
        print("\nBilling Management")
   

        

def generate_bill():
    bill_id = input("Enter Bill ID: ")
    patient_id = input("Enter Patient ID: ")
    amount = input("Enter Amount: ")
    database.add_bill(bill_id, patient_id, amount)

def view_bills():
    bills = database.get_bills()
    for bill in bills:
        print(bill)
