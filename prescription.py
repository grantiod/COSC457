from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Prescription:
    def __init__(self):
        self.root = Tk()
        self.root.title('Prescription')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        med = self.med_id_e.get()
        self.med_id_e.delete(0, END)
        qty = self.qty_e.get()
        self.qty_e.delete(0, END)
        refills = self.refills_e.get()
        self.refills_e.delete(0, END)
        pharm_name = self.pharmacy_name_e.get()
        self.pharmacy_name_e.delete(0, END)
        pharm_add = self.pharmacy_address_e.get()
        self.pharmacy_address_e.delete(0, END)
        date = self.date_e.get()
        self.date_e.delete(0, END)
        e_id = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)
        p_id = self.patient_id_e.get()
        self.patient_id_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO PRESCRIPTION VALUES (" + med + "," + qty + ",\"" + refills + "\",\"" + pharm_name + "\",\"" + pharm_add + "\",\"" + date + "\"," + e_id + "," + p_id + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.med_id_lbl = Label(self.root, text='Medicine ID:')
        self.med_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.med_id_e = Entry(self.root, width=10, borderwidth=1)
        self.med_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.qty_lbl = Label(self.root, text='Quantity:')
        self.qty_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.qty_e = Entry(self.root, width=10, borderwidth=1)
        self.qty_e.grid(row=0, column=3, padx=5, pady=5)

        self.refills_lbl = Label(self.root, text='Refills:')
        self.refills_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.refills_e = Entry(self.root, width=10, borderwidth=1)
        self.refills_e.grid(row=0, column=5, padx=5, pady=5)

        self.pharmacy_name_lbl = Label(self.root, text='Pharmacy Name:')
        self.pharmacy_name_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.pharmacy_name_e = Entry(self.root, width=10, borderwidth=1)
        self.pharmacy_name_e.grid(row=0, column=7, padx=5, pady=5)

        self.pharmacy_address_lbl = Label(self.root, text='Pharmacy Address:')
        self.pharmacy_address_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.pharmacy_address_e = Entry(self.root, width=10, borderwidth=1)
        self.pharmacy_address_e.grid(row=0, column=9, padx=5, pady=5)

        self.date_lbl = Label(self.root, text='Date Sent:')
        self.date_lbl.grid(row=0, column=10, padx=5, pady=5)
        self.date_e = Entry(self.root, width=10, borderwidth=1)
        self.date_e.grid(row=0, column=11, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee ID:')
        self.employee_num_lbl.grid(row=0, column=12, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=13, padx=5, pady=5)

        self.patient_id_lbl = Label(self.root, text='Patient ID:')
        self.patient_id_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.patient_id_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_id_e.grid(row=0, column=9, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    k = Prescription()
    k.run()