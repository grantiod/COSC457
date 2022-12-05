from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Referrals:
    def __init__(self):
        self.root = Tk()
        self.root.title('Referrals')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        address = self.address_e.get()
        self.address_e.delete(0, END)
        phone = self.phone_e.get()
        self.phone_e.delete(0, END)
        accepted_insur = self.accepted_insurances_e.get()
        self.accepted_insurances_e.delete(0, END)
        availability = self.availability_e.get()
        self.availability_e.delete(0, END)
        practice = self.practice_e.get()
        self.practice_e.delete(0, END)
        telehealth_offered = self.telehealth_offered_e.get()
        self.telehealth_offered_e.delete(0, END)
        patient_id = self.patient_id_e.get()
        self.patient_id_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO REFERRALS VALUES (\"" + address + "\",\"" + phone + "\",\"" + accepted_insur + "\",\"" + availability + "\",\"" + practice + "\",\"" + telehealth_offered + "\"," + patient_id + "," + employee_num + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.address_lbl = Label(self.root, text='Address:')
        self.address_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.address_e = Entry(self.root, width=10, borderwidth=1)
        self.address_e.grid(row=0, column=1, padx=5, pady=5)

        self.phone_lbl = Label(self.root, text='Phone:')
        self.phone_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.phone_e = Entry(self.root, width=10, borderwidth=1)
        self.phone_e.grid(row=0, column=3, padx=5, pady=5)

        self.accepted_insurances_lbl = Label(self.root, text='Accepted Insurances:')
        self.accepted_insurances_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.accepted_insurances_e = Entry(self.root, width=10, borderwidth=1)
        self.accepted_insurances_e.grid(row=0, column=5, padx=5, pady=5)

        self.availability_lbl = Label(self.root, text='Availability:')
        self.availability_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.availability_e = Entry(self.root, width=10, borderwidth=1)
        self.availability_e.grid(row=0, column=7, padx=5, pady=5)

        self.practice_lbl = Label(self.root, text='Practice:')
        self.practice_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.practice_e = Entry(self.root, width=10, borderwidth=1)
        self.practice_e.grid(row=0, column=9, padx=5, pady=5)

        self.telehealth_offered_lbl = Label(self.root, text='Telehealth Offered:')
        self.telehealth_offered_lbl.grid(row=0, column=10, padx=5, pady=5)
        self.telehealth_offered_e = Entry(self.root, width=10, borderwidth=1)
        self.telehealth_offered_e.grid(row=0, column=11, padx=5, pady=5)

        self.patient_id_lbl = Label(self.root, text='Patient ID:')
        self.patient_id_lbl.grid(row=0, column=12, padx=5, pady=5)
        self.patient_id_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_id_e.grid(row=0, column=13, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee Num:')
        self.employee_num_lbl.grid(row=0, column=14, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=15, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    r = Referrals()
    r.run()