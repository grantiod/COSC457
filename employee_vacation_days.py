from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Employee_Vacation_Days:
    def __init__(self):
        self.root = Tk()
        self.root.title('Employee Vacation Days')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        employee_name = self.employee_name_e.get()
        self.employee_name_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)
        dates_off = self.dates_off_e.get()
        self.dates_off_e.delete(0, END)
        num_allotted = self.num_days_allotted_e.get()
        self.num_days_allotted_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO EMPLOYEE_VACATION_DAYS VALUES (\"" + employee_name + "\"," + employee_num + ",\"" + dates_off + "\"," + num_allotted + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.employee_name_lbl = Label(self.root, text='Employee Name:')
        self.employee_name_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.employee_name_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_name_e.grid(row=0, column=1, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee Num:')
        self.employee_num_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=3, padx=5, pady=5)

        self.dates_off_lbl = Label(self.root, text='Dates Off:')
        self.dates_off_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.dates_off_e = Entry(self.root, width=10, borderwidth=1)
        self.dates_off_e.grid(row=0, column=5, padx=5, pady=5)

        self.num_days_allotted_lbl = Label(self.root, text='Number of Days Allotted:')
        self.num_days_allotted_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.num_days_allotted_e = Entry(self.root, width=10, borderwidth=1)
        self.num_days_allotted_e.grid(row=0, column=7, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    e = Employee_Vacation_Days()
    e.run()