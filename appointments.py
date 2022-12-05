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

        appintment_num = self.appointment_num_e.get()
        self.appointment_num_e.delete(0, END)
        patient_name = self.patient_name_e.get()
        self.patient_name_e.delete(0, END)
        patient_id = self.patient_id_e.get()
        self.patient_id_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO APPOINTMENTS VALUES (" + appintment_num + ",\"" + patient_name + "\"," + patient_id + "," + employee_num + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.appointment_num_lbl = Label(self.root, text='Appointment Num:')
        self.appointment_num_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.appointment_num_e = Entry(self.root, width=10, borderwidth=1)
        self.appointment_num_e.grid(row=0, column=1, padx=5, pady=5)

        self.patient_name_lbl = Label(self.root, text='Patient Name:')
        self.patient_name_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.patient_name_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_name_e.grid(row=0, column=3, padx=5, pady=5)

        self.patient_id_lbl = Label(self.root, text='Patient ID:')
        self.patient_id_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.patient_id_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_id_e.grid(row=0, column=5, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee Num:')
        self.employee_num_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=7, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    a = Appointments()
    a.run()