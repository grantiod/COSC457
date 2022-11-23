from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb
# add db import

class Employee:
    def __init__(self):
        self.root = Tk()
        self.root.title('Employee')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        ename = self.employee_name_e.get()
        self.employee_name_e.delete(0, END)
        enum = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)
        ssn = self.ssn_e.get()
        self.ssn_e.delete(0, END)
        dob = self.dob_e.get()
        self.dob_e.delete(0, END)
        add = self.address_e.get()
        self.address_e.delete(0, END)

        c = db.cursor()
        c.execute("INSERT INTO EMPLOYEE VALUES (" + ename + "," + str(enum) + "," + str(ssn) + "," + dob + "," + add + ")")
        c.close()

    def run(self):
        self.employee_name_lbl = Label(self.root, text='Employee Name:')
        self.employee_name_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.employee_name_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_name_e.grid(row=0, column=1, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee Num:')
        self.employee_num_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=3, padx=5, pady=5)

        self.ssn_lbl = Label(self.root, text='SSN:')
        self.ssn_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.ssn_e = Entry(self.root, width=10, borderwidth=1)
        self.ssn_e.grid(row=0, column=5, padx=5, pady=5)

        self.dob_lbl = Label(self.root, text='DoB:')
        self.dob_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.dob_e = Entry(self.root, width=10, borderwidth=1)
        self.dob_e.grid(row=0, column=7, padx=5, pady=5)

        self.address_lbl = Label(self.root, text='Address:')
        self.address_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.address_e = Entry(self.root, width=10, borderwidth=1)
        self.address_e.grid(row=0, column=9, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()