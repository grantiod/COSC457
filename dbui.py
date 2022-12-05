from tkinter import Tk, Button, mainloop
from employee import Employee
from patient import Patient
from dependent import Dependent
from student import Student
from medicine import Medicine
from branch import Branch
from equipment import Equipment
from inventory import Inventory
from office_room import Office_Room
from procedures import Procedures
from office_bills import Office_Bills
from business_accounts import Business_Accounts
from referrals import Referrals
from operations import Operations
from pharmacy import Pharmacy
from patient_health_insurance import Patient_Health_Insurance
from patient_bills import Patient_Bills
from patient_account import Patient_Account
from appointments import Appointments
from k_plan import K_Plan
from healthcare_worker import Healthcare_Worker
from employee_sick_days import Employee_Sick_Days
from employee_vacation_days import Employee_Vacation_Days
from employee_working_hours import Employee_Working_Hours
from employee_health_insurance import Employee_Health_Insurance
from sql import SQL

root = Tk()
root.title("Database UI")
root.geometry('1200x300')

# opens windows for respective tables
def employee():
    e = Employee()
    e.run()

def employee_health_insurance():
    e = Employee_Health_Insurance()
    e.run()

def employee_working_hours():
    e = Employee_Working_Hours()
    e.run()

def employee_vacation_days():
    e = Employee_Vacation_Days()
    e.run()

def employee_sick_days():
    e = Employee_Sick_Days()
    e.run()

def dependent():
    d = Dependent()
    d.run()

def student():
    s = Student()
    s.run()

def healthcare_worker():
    h = Healthcare_Worker()
    h.run()

def kplan():
    k = K_Plan()
    k.run()

def patient():
    p = Patient()
    p.run()

def appointment():
    a = Appointments()
    a.run()

def patient_account():
    p = Patient_Account()
    p.run()

def patient_bill():
    p = Patient_Bills()
    p.run()

def patient_health_insurance():
    p = Patient_Health_Insurance()
    p.run()

def operation():
    o = Operations()
    o.run()

def pharmacy():
    p = Pharmacy()
    p.run()

def medicine():
    m = Medicine()
    m.run()

def referral():
    r = Referrals()
    r.run()

def branch():
    b = Branch()
    b.run()

def business_acc():
    b = Business_Accounts()
    b.run()

def office_bill():
    o = Office_Bills()
    o.run()

def procedure():
    p = Procedures()
    p.run()

def office_room():
    o = Office_Room()
    o.run()

def inventory():
    i = Inventory()
    i.run()

def equipment():
    e = Equipment()
    e.run()

def sql():
    s = SQL()
    s.run()

# EMPLOYEE
employee_btn = Button(root, text="Employee", command=employee)
employee_btn.grid(row=0, column=0, padx=10, pady=10)

# EMPLOYEE HEALTH INSURANCE
employee_health_insur_btn = Button(root, text="Employee Health Insurance", command=employee_health_insurance)
employee_health_insur_btn.grid(row=0, column=1, padx=10, pady=10)

# EMPLOYEE WORKING HOURS
employee_working_hours_btn = Button(root, text="Employee Working Hours", command=employee_working_hours)
employee_working_hours_btn.grid(row=0, column=2, padx=10, pady=10)

# EMPLOYEE VACATION DAYS
employee_vacation_days_btn = Button(root, text="Employee Vacation Days", command=employee_vacation_days)
employee_vacation_days_btn.grid(row=0, column=3, padx=10, pady=10)

# EMPLOYEE SICK DAYS
employee_sick_days_btn = Button(root, text="Employee Sick Days", command=employee_sick_days)
employee_sick_days_btn.grid(row=0, column=4, padx=10, pady=10)

# DEPENDENT
dependent_btn = Button(root, text="Dependent", command=dependent)
dependent_btn.grid(row=0, column=5, padx=10, pady=10)

# STUDENT
student_btn = Button(root, text="Student", command=student)
student_btn.grid(row=0, column=6, padx=10, pady=10)

# HEALTHCARE WORKER
healthcare_worker_btn = Button(root, text="Healthcare Worker", command=healthcare_worker)
healthcare_worker_btn.grid(row=0, column=7, padx=10, pady=10)

# 401(k) PLAN
kplan_btn = Button(root, text="401(k) Plan", command=kplan)
kplan_btn.grid(row=0, column=8, padx=10, pady=10)

# PATIENT
patient_btn = Button(root, text="Patient", command=patient)
patient_btn.grid(row=1, column=0, padx=10, pady=10)

# APPOINTMENT
appointment_btn = Button(root, text="Appointment", command=appointment)
appointment_btn.grid(row=1, column=1, padx=10, pady=10)

# PATIENT ACCOUNT
patient_acc_btn = Button(root, text="Patient Account", command=patient_account)
patient_acc_btn.grid(row=1, column=2, padx=10, pady=10)

# PATIENT BILL
patient_bill_btn = Button(root, text="Patient Bill", command=patient_bill)
patient_bill_btn.grid(row=1, column=3, padx=10, pady=10)

# PATIENT HEALTH INSURANCE
patient_health_insur_btn = Button(root, text="Patient Health Insurance", command=patient_health_insurance)
patient_health_insur_btn.grid(row=1, column=4, padx=10, pady=10)

# OPERATION
operation_btn = Button(root, text="Operation", command=operation)
operation_btn.grid(row=1, column=5, padx=10, pady=10)

# PHARMACY
pharmacy_btn = Button(root, text="Pharmacy", command=pharmacy)
pharmacy_btn.grid(row=1, column=6, padx=10, pady=10)

# MEDICINE
medicine_btn = Button(root, text="Medicine", command=medicine)
medicine_btn.grid(row=1, column=7, padx=10, pady=10)

# REFERRALS
referral_btn = Button(root, text="Referral", command=referral)
referral_btn.grid(row=1, column=8, padx=10, pady=10)

# BRANCH
branch_btn = Button(root, text="Branch", command=branch)
branch_btn.grid(row=2, column=0, padx=10, pady=10)

# BUSINESS ACCOUNTS
business_acc_btn = Button(root, text="Business Account", command=business_acc)
business_acc_btn.grid(row=2, column=1, padx=10, pady=10)

# OFFICE BILLS
office_bill_btn = Button(root, text="Office Bill", command=office_bill)
office_bill_btn.grid(row=2, column=2, padx=10, pady=10)

# PROCEDURES
procedure_btn = Button(root, text="Procedure", command=procedure)
procedure_btn.grid(row=2, column=3, padx=10, pady=10)

# OFFICE ROOM
office_room_btn = Button(root, text="Office Room", command=office_room)
office_room_btn.grid(row=2, column=4, padx=10, pady=10)

# INVENTORY
inventory_btn = Button(root, text="Inventory", command=inventory)
inventory_btn.grid(row=2, column=5, padx=10, pady=10)

# EQUIPMENT
equipment_btn = Button(root, text="Equipment", command=equipment)
equipment_btn.grid(row=2, column=6, padx=10, pady=10)

# sql
sql_btn = Button(root, text="SQL", command=sql)
sql_btn.grid(row=3, column=0, padx=10, pady=10)

if __name__ == "__main__":
    root.mainloop()