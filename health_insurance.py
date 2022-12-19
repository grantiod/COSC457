from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Health_Insurance:
    def __init__(self):
        self.root = Tk()
        self.root.title('Health Insurance')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        insur_id = self.insur_id_e.get()
        self.insur_id_e.delete(0, END)
        name = self.insur_name_e.get()
        self.insur_name_e.delete(0, END)
        phone = self.phone_e.get()
        self.phone_e.delete(0, END)
        ssn = self.ssn_e.get()
        self.ssn_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO HEALTH_INSURANCE VALUES (" + insur_id + ",\"" + name + "\"," + phone + "," + ssn + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.insur_id_lbl = Label(self.root, text='Insurance ID:')
        self.insur_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.insur_id_e = Entry(self.root, width=10, borderwidth=1)
        self.insur_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.insur_name_lbl = Label(self.root, text='Insurance Name:')
        self.insur_name_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.insur_name_e = Entry(self.root, width=10, borderwidth=1)
        self.insur_name_e.grid(row=0, column=3, padx=5, pady=5)

        self.phone_lbl = Label(self.root, text='Insurance Phone:')
        self.phone_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.phone_e = Entry(self.root, width=10, borderwidth=1)
        self.phone_e.grid(row=0, column=5, padx=5, pady=5)

        self.ssn_lbl = Label(self.root, text='SSN:')
        self.ssn_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.ssn_e = Entry(self.root, width=10, borderwidth=1)
        self.ssn_e.grid(row=0, column=7, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    e = Health_Insurance()
    e.run()