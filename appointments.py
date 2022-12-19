from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Appointments:
    def __init__(self):
        self.root = Tk()
        self.root.title('Appointments')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        patient_id = self.patient_id_e.get()
        self.patient_id_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)
        date = self.date_e.get()
        self.date_e.delete(0, END)
        service_num = self.service_num_e.get()
        self.service_num_e.delete(0, END)
        branch_num = self.branch_num_e.get()
        self.branch_num_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO APPOINTMENTS VALUES (" + patient_id + "," + employee_num + ",\"" + date + "\"," + service_num + "," + branch_num + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.patient_id_lbl = Label(self.root, text='Patient ID:')
        self.patient_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.patient_id_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee ID:')
        self.employee_num_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=3, padx=5, pady=5)

        self.date_lbl = Label(self.root, text='Appointment Date:')
        self.date_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.date_e = Entry(self.root, width=10, borderwidth=1)
        self.date_e.grid(row=0, column=5, padx=5, pady=5)

        self.service_num_lbl = Label(self.root, text='Service Num:')
        self.service_num_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.service_num_e = Entry(self.root, width=10, borderwidth=1)
        self.service_num_e.grid(row=0, column=7, padx=5, pady=5)

        self.branch_num_lbl = Label(self.root, text='Branch Num:')
        self.branch_num_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.branch_num_e = Entry(self.root, width=10, borderwidth=1)
        self.branch_num_e.grid(row=0, column=9, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    a = Appointments()
    a.run()