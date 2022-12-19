from tkinter import Entry, Button, Tk, END, mainloop, Label, Toplevel
import MySQLdb

class Get_Appt:
    def __init__(self):
        self.root = Tk()
        self.root.title('Get Appointments')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        c = db.cursor()
        c.execute('USE psych_office_DB')

        date = self.date_e.get()

        try:
            toplevel = Toplevel()
            c.execute("select a.patient_id, a.employee_id, a.branch_num, s.s_name from appointment a inner join service s on s.s_num = a.service_num where " + date + " = appointment_date")
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
        self.date_lbl = Label(self.root, text='Date:')
        self.date_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.date_e = Entry(self.root, width=10, borderwidth=1)
        self.date_e.grid(row=0, column=1, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Get_Meds()
    d.run()