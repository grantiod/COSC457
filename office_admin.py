from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Office_Admin:
    def __init__(self):
        self.root = Tk()
        self.root.title('Office Admin')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        salary = self.salary_e.get()
        self.salary_e.delete(0, END)
        has_degree = self.has_degree_e.get()
        self.has_degree_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO OFFICE_ADMIN VALUES (" + employee_num + ",\"" + has_degree + "\"," + salary + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.employee_num_lbl = Label(self.root, text='Employee ID:')
        self.employee_num_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=1, padx=5, pady=5)

        self.has_degree_lbl = Label(self.root, text='Has Degree:')
        self.has_degree_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.has_degree_e = Entry(self.root, width=10, borderwidth=1)
        self.has_degree_e.grid(row=0, column=3, padx=5, pady=5)

        self.salary_lbl = Label(self.root, text='Salary:')
        self.salary_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.salary_e = Entry(self.root, width=10, borderwidth=1)
        self.salary_e.grid(row=0, column=5, padx=5, pady=5)        

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Office_Admin()
    d.run()