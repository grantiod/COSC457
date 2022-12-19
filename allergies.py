from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Allergies:
    def __init__(self):
        self.root = Tk()
        self.root.title('Allergies')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        patient_id = self.patient_id_e.get()
        self.patient_id_e.delete(0, END)
        alergy = self.allergy_e.get()
        self.allergy_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO ALLERGIES VALUES (" + patient_id + ",\"" + alergy + "\")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.patient_id_lbl = Label(self.root, text='Patient ID:')
        self.patient_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.patient_id_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.allergy_lbl = Label(self.root, text='Allergy:')
        self.allergy_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.allergy_e = Entry(self.root, width=10, borderwidth=1)
        self.allergy_e.grid(row=0, column=3, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Allergies()
    d.run()