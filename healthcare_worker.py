from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Healthcare_Worker:
    def __init__(self):
        self.root = Tk()
        self.root.title('Healthcare Worker')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)
        title = self.title_e.get()
        self.title_e.delete(0, END)
        num_patients = self.num_patients_e.get()
        self.num_patients_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO HEALTHCARE_WORKER VALUES (" + employee_num + ",\"" + title + "\"," + num_patients + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.employee_num_lbl = Label(self.root, text='Employee Num:')
        self.employee_num_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=1, padx=5, pady=5)

        self.title_lbl = Label(self.root, text='Title:')
        self.title_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.title_e = Entry(self.root, width=10, borderwidth=1)
        self.title_e.grid(row=0, column=3, padx=5, pady=5)

        self.num_patients_lbl = Label(self.root, text='Number of Patients:')
        self.num_patients_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.num_patients_e = Entry(self.root, width=10, borderwidth=1)
        self.num_patients_e.grid(row=0, column=5, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    h = Healthcare_Worker()
    h.run()