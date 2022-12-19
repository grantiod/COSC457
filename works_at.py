from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Works_At:
    def __init__(self):
        self.root = Tk()
        self.root.title('Works At')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        hours = self.shift_hours_e.get()
        self.shift_hours_e.delete(0, END)
        date = self.shift_date_lbl.get()
        self.shift_date_lbl.delete(0, END)
        e_id = self.employee_id_e.get()
        self.employee_id_e.delete(0, END)
        branch = self.branch_num_e.get()
        self.branch_num_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO WORKS_AT VALUES (" + hours + ",\"" + date + "\"," + e_id + "," + branch + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.shift_hours_lbl = Label(self.root, text='Shift Hours:')
        self.shift_hours_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.shift_hours_e = Entry(self.root, width=10, borderwidth=1)
        self.shift_hours_e.grid(row=0, column=1, padx=5, pady=5)

        self.shift_date_lbl = Label(self.root, text='Shift Date:')
        self.shift_date_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.shift_date_e = Entry(self.root, width=10, borderwidth=1)
        self.shift_date_e.grid(row=0, column=3, padx=5, pady=5)

        self.employee_id_lbl = Label(self.root, text='Employee ID:')
        self.employee_id_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.employee_id_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_id_e.grid(row=0, column=5, padx=5, pady=5)

        self.branch_num_lbl = Label(self.root, text='Branch Num:')
        self.branch_num_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.branch_num_e = Entry(self.root, width=10, borderwidth=1)
        self.branch_num_e.grid(row=0, column=7, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Works_At()
    d.run()