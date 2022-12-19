from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Emergency_Contact:
    def __init__(self):
        self.root = Tk()
        self.root.title('Emergency Contact')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        name = self.name_e.get()
        self.name_e.delete(0, END)
        phone = self.phone_e.get()
        self.phone_e.delete(0, END)
        ssn = self.ssn_e.get()
        self.ssn_e.delete(0, END)
        rel = self.rel_e.get()
        self.rel_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO EMERGENCY_CONTACT VALUES (\"" + name + "\"," + phone + "," + ssn + ",\"" + rel + "\")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.name_lbl = Label(self.root, text='Contact Name:')
        self.name_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.name_e = Entry(self.root, width=10, borderwidth=1)
        self.name_e.grid(row=0, column=1, padx=5, pady=5)

        self.phone_lbl = Label(self.root, text='Phone:')
        self.phone_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.phone_e = Entry(self.root, width=10, borderwidth=1)
        self.phone_e.grid(row=0, column=3, padx=5, pady=5)

        self.ssn_lbl = Label(self.root, text='SSN:')
        self.ssn_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.ssn_e = Entry(self.root, width=10, borderwidth=1)
        self.ssn_e.grid(row=0, column=5, padx=5, pady=5)

        self.rel_lbl = Label(self.root, text='Relationship:')
        self.rel_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.rel_e = Entry(self.root, width=10, borderwidth=1)
        self.rel_e.grid(row=0, column=7, padx=5, pady=5)  

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Emergency_Contact()
    d.run()