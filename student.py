from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Student:
    def __init__(self):
        self.root = Tk()
        self.root.title('Student')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        student_id = self.student_id_e.get()
        self.student_id_e.delete(0, END)
        student_name = self.student_name_e.get()
        self.student_name_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO STUDENT VALUES (" + student_id + ",\"" + student_name + "\"," + employee_num + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.student_id_lbl = Label(self.root, text='Student ID:')
        self.student_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.student_id_e = Entry(self.root, width=10, borderwidth=1)
        self.student_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.student_name_lbl = Label(self.root, text='Student Name:')
        self.student_name_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.student_name_e = Entry(self.root, width=10, borderwidth=1)
        self.student_name_e.grid(row=0, column=3, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee Num:')
        self.employee_num_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=5, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Student()
    d.run()