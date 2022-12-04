from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Medicine:
    def __init__(self):
        self.root = Tk()
        self.root.title('Medicine')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        medication_id = self.medication_id_e.get()
        self.medication_id_e.delete(0, END)
        manufacturer = self.manufacturer_e.get()
        self.manufacturer_e.delete(0, END)
        prescription_amount = self.prescription_amount_e.get()
        self.prescription_amount_e.delete(0, END)
        prescription_date = self.prescription_date_e.get()
        self.prescription_date_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete()
        patient_name = self.patient_name_e.get()
        self.patient_name_e.delete(0, END)
        patient_id = self.patient_id_e.get()
        self.patient_id_e.delete(0, END)
        
        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO MEDICATIONS VALUES (" + medication_id + ",\"" + manufacturer + "\"," + prescription_amount + ",\"" + prescription_date + "\"," + employee_num + ",\"" + patient_name + "\"," + patient_id + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.medication_id_lbl = Label(self.root, text='Medication ID:')
        self.medication_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.medication_id_e = Entry(self.root, width=10, borderwidth=1)
        self.medication_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.manufacturer_lbl = Label(self.root, text='Manufacturer:')
        self.manufacturer_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.manufacturer_e = Entry(self.root, width=10, borderwidth=1)
        self.manufacturer_e.grid(row=0, column=3, padx=5, pady=5)

        self.prescription_amount_lbl = Label(self.root, text='Prescription Amount:')
        self.prescription_amount_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.prescription_amount_e = Entry(self.root, width=10, borderwidth=1)
        self.prescription_amount_e.grid(row=0, column=5, padx=5, pady=5)

        self.prescription_date_lbl = Label(self.root, text='Prescription Date:')
        self.prescription_date_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.prescription_date_e = Entry(self.root, width=10, borderwidth=1)
        self.prescription_date_e.grid(row=0, column=7, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee Num:')
        self.employee_num_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=9, padx=5, pady=5)

        self.patient_name_lbl = Label(self.root, text='Patient Name:')
        self.patient_name_lbl.grid(row=0, column=10, padx=5, pady=5)
        self.patient_name_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_name_e.grid(row=0, column=11, padx=5, pady=5)

        self.patient_id_lbl = Label(self.root, text='Patient ID:')
        self.patient_id_lbl.grid(row=0, column=12, padx=5, pady=5)
        self.patient_id_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_id_e.grid(row=0, column=13, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Medicine()
    d.run()