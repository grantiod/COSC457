from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Employee:
    def __init__(self):
        self.root = Tk()
        self.root.title('Employee')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        enum = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)
        ssn = self.ssn_e.get()
        self.ssn_e.delete(0, END)
        mentor = self.ismentor_e.get()
        self.ismentor_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO EMPLOYEE VALUES (" + enum + "," + ssn + "," + mentor + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.employee_num_lbl = Label(self.root, text='Employee ID:')
        self.employee_num_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=1, padx=5, pady=5)

        self.ssn_lbl = Label(self.root, text='SSN:')
        self.ssn_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.ssn_e = Entry(self.root, width=10, borderwidth=1)
        self.ssn_e.grid(row=0, column=3, padx=5, pady=5)

        self.ismentor_lbl = Label(self.root, text='Is Mentor:')
        self.ismentor_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.ismentor_e = Entry(self.root, width=10, borderwidth=1)
        self.ismentor_e.grid(row=0, column=5, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    e = Employee()
    e.run()