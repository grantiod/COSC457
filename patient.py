from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Patient:
    def __init__(self):
        self.root = Tk()
        self.root.title('Patient')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        patient_id = self.patient_id_e.get()
        self.patient_id_e.delete(0, END)
        patient_name = self.patient_name_e.get()
        self.patient_name_e.delete(0, END)
        emergency_contact = self.emergency_contact_e.get()
        self.emergency_contact_e.delete(0, END)
        dob = self.dob_e.get()
        self.dob_e.delete()
        phone = self.phone_e.get()
        self.phone_e.delete(0, END)
        email = self.email_e.get()
        self.email_e.delete(0, END)
        address = self.address_e.get()
        self.address_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO PATIENT VALUES (" + patient_id + ",\"" + patient_name + "\",\"" + emergency_contact + "\",\"" + dob + "\",\"" + phone + "\",\"" + email + "\",\"" + address + "\")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.patient_id_lbl = Label(self.root, text='Patient ID:')
        self.patient_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.patient_id_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.patient_name_lbl = Label(self.root, text='Patient Name:')
        self.patient_name_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.patient_name_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_name_e.grid(row=0, column=3, padx=5, pady=5)

        self.emergency_contact_lbl = Label(self.root, text='Emergency Contact:')
        self.emergency_contact_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.emergency_contact_e = Entry(self.root, width=10, borderwidth=1)
        self.emergency_contact_e.grid(row=0, column=5, padx=5, pady=5)

        self.dob_lbl = Label(self.root, text='DoB:')
        self.dob_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.dob_e = Entry(self.root, width=10, borderwidth=1)
        self.dob_e.grid(row=0, column=7, padx=5, pady=5)

        self.phone_lbl = Label(self.root, text='Phone:')
        self.phone_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.phone_e = Entry(self.root, width=10, borderwidth=1)
        self.phone_e.grid(row=0, column=9, padx=5, pady=5)

        self.email_lbl = Label(self.root, text='Email:')
        self.email_lbl.grid(row=0, column=10, padx=5, pady=5)
        self.email_e = Entry(self.root, width=10, borderwidth=1)
        self.email_e.grid(row=0, column=11, padx=5, pady=5)

        self.address_lbl = Label(self.root, text='Address:')
        self.address_lbl.grid(row=0, column=12, padx=5, pady=5)
        self.address_e = Entry(self.root, width=10, borderwidth=1)
        self.address_e.grid(row=0, column=13, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    p = Patient()
    p.run()