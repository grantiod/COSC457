from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Intern:
    def __init__(self):
        self.root = Tk()
        self.root.title('Intern')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        mentor = self.mentor_id_e.get()
        self.mentor_id_e.delete(0, END)
        school = self.school_e.get()
        self.school_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO INTERN VALUES (" + employee_num + ",\"" + school + "\"," + mentor + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.employee_num_lbl = Label(self.root, text='Employee Num:')
        self.employee_num_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=1, padx=5, pady=5)

        self.school_lbl = Label(self.root, text='School Name:')
        self.school_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.school_e = Entry(self.root, width=10, borderwidth=1)
        self.school_e.grid(row=0, column=3, padx=5, pady=5)

        self.mentor_id_lbl = Label(self.root, text='Mentor ID:')
        self.mentor_id_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.mentor_id_e = Entry(self.root, width=10, borderwidth=1)
        self.mentor_id_e.grid(row=0, column=5, padx=5, pady=5)        

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Intern()
    d.run()