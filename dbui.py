from tkinter import Tk, Button, mainloop
from employee import Employee
from patient import Patient
from intern import Intern
from medication import Medication
from branch import Branch
from equipment import Equipment
from inventory import Inventory
from referral import Referral
from patient_bill import Patient_Bill
from appointments import Appointments
from k_plan import K_Plan
from healthcare_worker import Healthcare_Worker
from health_insurance import Health_Insurance
from person import Person
from office_admin import Office_Admin
from emergency_contact import Emergency_Contact
from allergies import Allergies
from service import Service
from prescription import Prescription
from department import Department
from works_at import Works_At
from paid_leave import Paid_Leave
from office_bill import Office_Bill
from getmeds import Get_Meds
from getappointments import Get_Appt
from getemergencycontact import Get_EC
from sql import SQL

root = Tk()
root.title("Database UI")
root.geometry('900x300')

# opens windows for respective tables
def employee():
    e = Employee()
    e.run()

def health_insurance():
    e = Health_Insurance()
    e.run()

def intern():
    i = Intern()
    i.run()

def healthcare_worker():
    h = Healthcare_Worker()
    h.run()

def kplan():
    k = K_Plan()
    k.run()

def person():
    p = Person()
    p.run()

def patient():
    p = Patient()
    p.run()

def appointment():
    a = Appointments()
    a.run()

def patient_bill():
    p = Patient_Bill()
    p.run()

def medicine():
    m = Medication()
    m.run()

def referral():
    r = Referral()
    r.run()

def branch():
    b = Branch()
    b.run()

def inventory():
    i = Inventory()
    i.run()

def equipment():
    e = Equipment()
    e.run()

def admin():
    a = Office_Admin()
    a.run()

def contact():
    c = Emergency_Contact()
    c.run()

def allergies():
    a = Allergies()
    a.run()

def service():
    s = Service()
    s.run()

def prescription():
    p = Prescription()
    p.run()

def department():
    d = Department()
    d.run()

def works():
    w = Works_At()
    w.run()

def leave():
    l = Paid_Leave()
    l.run()

def bill():
    o = Office_Bill()
    o.run()

def sql():
    s = SQL()
    s.run()

def getmeds():
    g = Get_Meds()
    g.run()

def getappt():
    g = Get_Appt()
    g.run()

def getec():
    g = Get_EC()
    g.run()

# EMPLOYEE
employee_btn = Button(root, text="Employee", command=employee)
employee_btn.grid(row=0, column=0, padx=10, pady=10)

# HEALTH INSURANCE
health_insur_btn = Button(root, text="Health Insurance", command=health_insurance)
health_insur_btn.grid(row=0, column=1, padx=10, pady=10)

# INTERN
intern_btn = Button(root, text="Intern", command=intern)
intern_btn.grid(row=0, column=2, padx=10, pady=10)

# HEALTHCARE WORKER
healthcare_worker_btn = Button(root, text="Healthcare Worker", command=healthcare_worker)
healthcare_worker_btn.grid(row=0, column=3, padx=10, pady=10)

# 401(k) PLAN
kplan_btn = Button(root, text="401(k) Plan", command=kplan)
kplan_btn.grid(row=0, column=4, padx=10, pady=10)

# PERSON
person_btn = Button(root, text="Person", command=person)
person_btn.grid(row=0, column=5, padx=10, pady=10)

# WORKS_AT
works_btn = Button(root, text="Works At", command=works)
works_btn.grid(row=0, column=6, padx=10, pady=10)

# PAID LEAVE
leave_btn = Button(root, text="Paid Leave", command=leave)
leave_btn.grid(row=0, column=7, padx=10, pady=10)

# PATIENT
patient_btn = Button(root, text="Patient", command=patient)
patient_btn.grid(row=1, column=0, padx=10, pady=10)

# APPOINTMENT
appointment_btn = Button(root, text="Appointment", command=appointment)
appointment_btn.grid(row=1, column=1, padx=10, pady=10)

# PATIENT BILL
patient_bill_btn = Button(root, text="Patient Bill", command=patient_bill)
patient_bill_btn.grid(row=1, column=2, padx=10, pady=10)

# MEDICINE
medicine_btn = Button(root, text="Medications", command=medicine)
medicine_btn.grid(row=1, column=3, padx=10, pady=10)

# REFERRALS
referral_btn = Button(root, text="Referral", command=referral)
referral_btn.grid(row=1, column=4, padx=10, pady=10)

# ALLERGIES
allergies_btn = Button(root, text="Allergies", command=allergies)
allergies_btn.grid(row=1, column=5, padx=10, pady=10)

# PRESCRIPTION
prescription_btn = Button(root, text="Prescription", command=prescription)
prescription_btn.grid(row=1, column=6, padx=10, pady=10)

# BRANCH
branch_btn = Button(root, text="Branch", command=branch)
branch_btn.grid(row=2, column=0, padx=10, pady=10)

# INVENTORY
inventory_btn = Button(root, text="Inventory", command=inventory)
inventory_btn.grid(row=2, column=1, padx=10, pady=10)

# EQUIPMENT
equipment_btn = Button(root, text="Equipment", command=equipment)
equipment_btn.grid(row=2, column=2, padx=10, pady=10)

# OFFICE ADMIN
admin_btn = Button(root, text="Office Admin", command=admin)
admin_btn.grid(row=2, column=3, padx=10, pady=10)

# EMERGENCY CONTACT
contact_btn = Button(root, text="Emergency Contact", command=contact)
contact_btn.grid(row=2, column=4, padx=10, pady=10)

# SERVICE
service_btn = Button(root, text="Service", command=service)
service_btn.grid(row=2, column=5, padx=10, pady=10)

# DEPARTMENT
department_btn = Button(root, text="Department", command=department)
department_btn.grid(row=2, column=6, padx=10, pady=10)

# OFFICE BILL
o_bill_btn = Button(root, text="Office Bill", command=bill)
o_bill_btn.grid(row=2, column=7, padx=10, pady=10)

# sql
sql_btn = Button(root, text="SQL", command=sql)
sql_btn.grid(row=3, column=0, padx=10, pady=10)

# get meds
getmeds_btn = Button(root, text="Get Meds", command=getmeds)
getmeds_btn.grid(row=3, column=1, padx=10, pady=10)

# get appointments
getappt_btn = Button(root, text="Get Appointments", command=getappt)
getappt_btn.grid(row=3, column=2, padx=10, pady=10)

# get emergency contact
getec_btn = Button(root, text="Get Emergency Contact", command=getec)
getec_btn.grid(row=3, column=3, padx=10, pady=10)

if __name__ == "__main__":
    root.mainloop()