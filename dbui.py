from tkinter import Tk, Button, mainloop, Text
from employee import Employee
from patient import Patient
from sql import SQL

root = Tk()
root.title("Database UI")
root.geometry('1000x1000')

# opens windows for respective tables
def employee():
    e = Employee()
    e.run()

def dependent():
    pass

def student():
    pass

def patient():
    p = Patient()
    p.run()

def medicine():
    pass

def branch():
    pass

def sql():
    s = SQL()
    s.run()

# EMPLOYEE
employee_btn = Button(root, text="Employee", command=employee)
employee_btn.grid(row=0, column=0, padx=10, pady=10)

# DEPENDENT
dependent_btn = Button(root, text="Dependent", command=dependent)
dependent_btn.grid(row=0, column=1, padx=10, pady=10)

# STUDENT
student_btn = Button(root, text="Student", command=student)
student_btn.grid(row=0, column=2, padx=10, pady=10)

# PATIENT
patient_btn = Button(root, text="Patient", command=patient)
patient_btn.grid(row=1, column=0, padx=10, pady=10)

# MEDICINE
medicine_btn = Button(root, text="Medicine", command=medicine)
medicine_btn.grid(row=1, column=1, padx=10, pady=10)

# BRANCH
branch_btn = Button(root, text="Branch", command=branch)
branch_btn.grid(row=2, column=0, padx=10, pady=10)

# sql
sql_btn = Button(root, text="SQL", command=sql)
sql_btn.grid(row=10, column=0, padx=10, pady=10)

if __name__ == "__main__":
    root.mainloop()