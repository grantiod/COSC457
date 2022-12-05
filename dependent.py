from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Dependent:
    def __init__(self):
        self.root = Tk()
        self.root.title('Dependent')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        dependent_name = self.dependent_name_e.get()
        self.dependent_name_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)
        dep_dob = self.dep_dob_e.get()
        self.dep_dob_e.delete(0, END)
        address = self.address_e.get()
        self.address_e.delete(0, END)
        relationship = self.relationship_e.get()
        self.relationship_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO DEPENDENTS VALUES (\"" + dependent_name + "\"," + employee_num + ",\"" + dep_dob + "\",\"" + address + "\",\"" + relationship + "\")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.dependent_name_lbl = Label(self.root, text='Dependent Name:')
        self.dependent_name_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.dependent_name_e = Entry(self.root, width=10, borderwidth=1)
        self.dependent_name_e.grid(row=0, column=1, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee Num:')
        self.employee_num_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=3, padx=5, pady=5)

        self.dep_dob_lbl = Label(self.root, text='DoB:')
        self.dep_dob_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.dep_dob_e = Entry(self.root, width=10, borderwidth=1)
        self.dep_dob_e.grid(row=0, column=5, padx=5, pady=5)

        self.address_lbl = Label(self.root, text='Address:')
        self.address_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.address_e = Entry(self.root, width=10, borderwidth=1)
        self.address_e.grid(row=0, column=7, padx=5, pady=5)

        self.relationship_lbl = Label(self.root, text='Relationship:')
        self.relationship_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.relationship_e = Entry(self.root, width=10, borderwidth=1)
        self.relationship_e.grid(row=0, column=9, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Dependent()
    d.run()