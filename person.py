from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Person:
    def __init__(self):
        self.root = Tk()
        self.root.title('Person')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        ssn = self.ssn_e.get()
        self.ssn_e.delete(0, END)
        fname = self.fname_e.get()
        self.fname_e.delete(0, END)
        lname = self.lname_e.get()
        self.lname_e.delete(0, END)
        dob = self.dob_e.get()
        self.dob_e.delete(0, END)
        cellular = self.cellular_e.get()
        self.cellular_e.delete(0, END)
        street = self.street_e.get()
        self.street_e.delete(0, END)
        city = self.city_e.get()
        self.city_e.delete(0, END)
        state = self.state_e.get()
        self.state_e.delete(0, END)
        email = self.email_e.get()
        self.email_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO PERSON VALUES (" + ssn + ",\"" + fname + "\",\"" + lname + "\",\"" + dob + "\",\"" + cellular + "\",\"" + street + "\",\"" + city + "\",\"" + state + "\",\"" + email + "\")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.ssn_lbl = Label(self.root, text='SSN:')
        self.ssn_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.ssn_e = Entry(self.root, width=10, borderwidth=1)
        self.ssn_e.grid(row=0, column=1, padx=5, pady=5)

        self.fname_lbl = Label(self.root, text='First Name:')
        self.fname_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.fname_e = Entry(self.root, width=10, borderwidth=1)
        self.fname_e.grid(row=0, column=3, padx=5, pady=5)

        self.lname_lbl = Label(self.root, text='Last Name:')
        self.lname_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.lname_e = Entry(self.root, width=10, borderwidth=1)
        self.lname_e.grid(row=0, column=5, padx=5, pady=5)

        self.dob_lbl = Label(self.root, text='DoB:')
        self.dob_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.dob_e = Entry(self.root, width=10, borderwidth=1)
        self.dob_e.grid(row=0, column=7, padx=5, pady=5)

        self.cellular_lbl = Label(self.root, text='Cellular:')
        self.cellular_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.cellular_e = Entry(self.root, width=10, borderwidth=1)
        self.cellular_e.grid(row=0, column=9, padx=5, pady=5)

        self.street_lbl = Label(self.root, text='Street:')
        self.street_lbl.grid(row=0, column=10, padx=5, pady=5)
        self.street_e = Entry(self.root, width=10, borderwidth=1)
        self.street_e.grid(row=0, column=11, padx=5, pady=5)

        self.city_lbl = Label(self.root, text='City:')
        self.city_lbl.grid(row=0, column=12, padx=5, pady=5)
        self.city_e = Entry(self.root, width=10, borderwidth=1)
        self.city_e.grid(row=0, column=13, padx=5, pady=5)

        self.state_lbl = Label(self.root, text='State:')
        self.state_lbl.grid(row=0, column=14, padx=5, pady=5)
        self.state_e = Entry(self.root, width=10, borderwidth=1)
        self.state_e.grid(row=0, column=15, padx=5, pady=5)

        self.email_lbl = Label(self.root, text='Email:')
        self.email_lbl.grid(row=0, column=16, padx=5, pady=5)
        self.email_e = Entry(self.root, width=10, borderwidth=1)
        self.email_e.grid(row=0, column=17, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    p = Person()
    p.run()