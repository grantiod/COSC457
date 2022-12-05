from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Healthcare_Worker:
    def __init__(self):
        self.root = Tk()
        self.root.title('Healthcare Worker')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        ssn = self.ssn_e.get()
        self.ssn_e.delete(0, END)
        role = self.role_e.get()
        self.role_e.delete(0, END)
        address = self.address_e.get()
        self.address_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)
        num_patients = self.num_patients_e.get()
        self.num_patients_e.delete(0, END)
        employee_name = self.employee_name_e.get()
        self.employee_name_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO HEALTHCARE_WORKERS VALUES (" + ssn + ",\"" + role + "\",\"" + address + "\"," + employee_num + "," + num_patients + ",\"" + employee_name + "\")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.ssn_lbl = Label(self.root, text='SSN:')
        self.ssn_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.ssn_e = Entry(self.root, width=10, borderwidth=1)
        self.ssn_e.grid(row=0, column=1, padx=5, pady=5)

        self.role_lbl = Label(self.root, text='Role:')
        self.role_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.role_e = Entry(self.root, width=10, borderwidth=1)
        self.role_e.grid(row=0, column=3, padx=5, pady=5)

        self.address_lbl = Label(self.root, text='Address:')
        self.address_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.address_e = Entry(self.root, width=10, borderwidth=1)
        self.address_e.grid(row=0, column=5, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee Num:')
        self.employee_num_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=7, padx=5, pady=5)

        self.num_patients_lbl = Label(self.root, text='Number of Patients:')
        self.num_patients_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.num_patients_e = Entry(self.root, width=10, borderwidth=1)
        self.num_patients_e.grid(row=0, column=9, padx=5, pady=5)

        self.employee_name_lbl = Label(self.root, text='Employee Name:')
        self.employee_name_lbl.grid(row=0, column=10, padx=5, pady=5)
        self.employee_name_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_name_e.grid(row=0, column=11, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    h = Healthcare_Worker()
    h.run()