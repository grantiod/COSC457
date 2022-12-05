from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Patient_Health_Insurance:
    def __init__(self):
        self.root = Tk()
        self.root.title('Patient Health Insurance')

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
        insurance_provider = self.insurance_provider_e.get()
        self.insurance_provider_e.delete(0, END)
        insurance_id = self.insurance_id_e.get()
        self.insurance_id_e.delete(0, END)
        date_exp = self.date_expires_e.get()
        self.date_expires_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO PATIENT_HEALTH_INSURANCE VALUES (" + patient_id + ",\"" + patient_name + "\",\"" + insurance_provider + "\"," + insurance_id + ",\"" + date_exp + "\")")
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

        self.insurance_provider_lbl = Label(self.root, text='Insurance Provider:')
        self.insurance_provider_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.insurance_provider_e = Entry(self.root, width=10, borderwidth=1)
        self.insurance_provider_e.grid(row=0, column=5, padx=5, pady=5)

        self.insurance_id_lbl = Label(self.root, text='Insurance ID:')
        self.insurance_id_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.insurance_id_e = Entry(self.root, width=10, borderwidth=1)
        self.insurance_id_e.grid(row=0, column=7, padx=5, pady=5)

        self.date_expires_lbl = Label(self.root, text='Expiration Date:')
        self.date_expires_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.date_expires_e = Entry(self.root, width=10, borderwidth=1)
        self.date_expires_e.grid(row=0, column=9, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    p = Patient_Health_Insurance()
    p.run()