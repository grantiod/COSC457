from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Medication:
    def __init__(self):
        self.root = Tk()
        self.root.title('Medication')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        medication_id = self.medication_id_e.get()
        self.medication_id_e.delete(0, END)
        name = self.name_e.get()
        self.name_e.delete(0, END)
        dosage = self.prescription_amount_e.get()
        self.prescription_amount_e.delete(0, END)
        
        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO MEDICATION VALUES (" + medication_id + ",\"" + name + "\"," + dosage + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.medication_id_lbl = Label(self.root, text='Medication ID:')
        self.medication_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.medication_id_e = Entry(self.root, width=10, borderwidth=1)
        self.medication_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.name_lbl = Label(self.root, text='Medication Name:')
        self.name_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.name_e = Entry(self.root, width=10, borderwidth=1)
        self.name_e.grid(row=0, column=3, padx=5, pady=5)

        self.prescription_amount_lbl = Label(self.root, text='Dosage:')
        self.prescription_amount_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.prescription_amount_e = Entry(self.root, width=10, borderwidth=1)
        self.prescription_amount_e.grid(row=0, column=5, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Medication()
    d.run()