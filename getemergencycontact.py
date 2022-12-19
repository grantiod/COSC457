from tkinter import Entry, Button, Tk, END, mainloop, Label, Toplevel
import MySQLdb

class Get_EC:
    def __init__(self):
        self.root = Tk()
        self.root.title('Get Emergency Contact')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        c = db.cursor()
        c.execute('USE psych_office_DB')

        employee_id = self.employee_id_e.get()

        try:
            toplevel = Toplevel()
            c.execute("select p.Fname, p.Lname, ec.ec_name, ec.ec_phone from Person p inner join emergency_contact ec on p.ssn = ec.ssn inner join employee e on e.ssn = p.ssn where " + employee_id + " = employee_id")
            output = c.fetchall()
            w = 0
            for x in output:
                output_lbl = Label(toplevel, text=w)
                output_lbl.grid(row=2, column=0, padx=5, pady=5)
        except:
            pass

        db.commit()
        c.close()
        db.close()

    def run(self):
        self.employee_id_lbl = Label(self.root, text='Employee ID:')
        self.employee_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.employee_id_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Get_EC()
    d.run()