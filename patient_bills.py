from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Patient_Bills:
    def __init__(self):
        self.root = Tk()
        self.root.title('Patient Bills')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        patient_name = self.patient_name_e.get()
        self.patient_name_e.delete(0, END)
        date = self.date_e.get()
        self.date_e.delete(0, END)
        payment_due = self.payment_due_e.get()
        self.payment_due_e.delete(0, END)
        cost = self.cost_e.get()
        self.cost_e.delete(0, END)
        patient_id = self.patient_id_e.get()
        self.patient_id_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO PATIENT_BILLS VALUES (\"" + patient_name + "\",\"" + date + "\",\"" + payment_due + "\"," + cost + "," + patient_id + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.patient_name_lbl = Label(self.root, text='Patient Name:')
        self.patient_name_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.patient_name_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_name_e.grid(row=0, column=1, padx=5, pady=5)

        self.date_lbl = Label(self.root, text='Date:')
        self.date_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.date_e = Entry(self.root, width=10, borderwidth=1)
        self.date_e.grid(row=0, column=3, padx=5, pady=5)

        self.payment_due_lbl = Label(self.root, text='Payment Due:')
        self.payment_due_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.payment_due_e = Entry(self.root, width=10, borderwidth=1)
        self.payment_due_e.grid(row=0, column=5, padx=5, pady=5)

        self.cost_lbl = Label(self.root, text='Cost:')
        self.cost_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.cost_e = Entry(self.root, width=10, borderwidth=1)
        self.cost_e.grid(row=0, column=7, padx=5, pady=5)

        self.patient_id_lbl = Label(self.root, text='Patient ID:')
        self.patient_id_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.patient_id_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_id_e.grid(row=0, column=9, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    p = Patient_Bills()
    p.run()