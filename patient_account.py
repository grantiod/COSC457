from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Patient_Account:
    def __init__(self):
        self.root = Tk()
        self.root.title('Patient Account')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        patient_id = self.patient_id_e.get()
        self.patient_id_e.delete(0, END)
        age = self.age_e.get()
        self.age_e.delete(0, END)
        patient_name = self.patient_name_e.get()
        self.patient_name_e.delete(0, END)
        phone = self.phone_e.get()
        self.phone_e.delete(0, END)
        address = self.address_e.get()
        self.address_e.delete(0, END)
        current_meds = self.current_meds_e.get()
        self.current_meds_e.delete(0, END)
        allergies = self.allergies_e.get()
        self.allergies_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO PATIENT_ACCOUNT VALUES (" + patient_id + "," + age + ",\"" + patient_name + "\",\"" + phone + "\",\"" + address + "\",\"" + current_meds + "\",\"" + allergies + "\")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.patient_id_lbl = Label(self.root, text='Patient ID:')
        self.patient_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.patient_id_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.age_lbl = Label(self.root, text='Age:')
        self.age_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.age_e = Entry(self.root, width=10, borderwidth=1)
        self.age_e.grid(row=0, column=3, padx=5, pady=5)

        self.patient_name_lbl = Label(self.root, text='Patient Name:')
        self.patient_name_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.patient_name_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_name_e.grid(row=0, column=5, padx=5, pady=5)

        self.phone_lbl = Label(self.root, text='Phone:')
        self.phone_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.phone_e = Entry(self.root, width=10, borderwidth=1)
        self.phone_e.grid(row=0, column=7, padx=5, pady=5)

        self.address_lbl = Label(self.root, text='Address:')
        self.address_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.address_e = Entry(self.root, width=10, borderwidth=1)
        self.address_e.grid(row=0, column=9, padx=5, pady=5)

        self.current_meds_lbl = Label(self.root, text='Current Medications:')
        self.current_meds_lbl.grid(row=0, column=10, padx=5, pady=5)
        self.current_meds_e = Entry(self.root, width=10, borderwidth=1)
        self.current_meds_e.grid(row=0, column=11, padx=5, pady=5)

        self.allergies_lbl = Label(self.root, text='Allergies:')
        self.allergies_lbl.grid(row=0, column=12, padx=5, pady=5)
        self.allergies_e = Entry(self.root, width=10, borderwidth=1)
        self.allergies_e.grid(row=0, column=13, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    p = Patient_Account()
    p.run()