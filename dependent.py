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

        c = db.cursor()
        c.execute('USE psych_office')
        c.close()

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