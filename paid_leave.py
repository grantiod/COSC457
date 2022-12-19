from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Paid_Leave:
    def __init__(self):
        self.root = Tk()
        self.root.title('Paid Leave')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        e_id = self.e_id_e.get()
        self.e_id_e.delete(0, END)
        date = self.date_e.get()
        self.date_e.delete(0, END)
        leave_type = self.type_e.get()
        self.type_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO PAID_LEAVE VALUES (" + e_id + ",\"" + date + "\",\"" + leave_type + "\")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.e_id_lbl = Label(self.root, text='Employee ID:')
        self.e_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.e_id_e = Entry(self.root, width=10, borderwidth=1)
        self.e_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.date_lbl = Label(self.root, text='Date Used:')
        self.date_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.date_e = Entry(self.root, width=10, borderwidth=1)
        self.date_e.grid(row=0, column=3, padx=5, pady=5)

        self.type_lbl = Label(self.root, text='Leave Type:')
        self.type_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.type_e = Entry(self.root, width=10, borderwidth=1)
        self.type_e.grid(row=0, column=5, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Paid_Leave()
    d.run()