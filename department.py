from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Department:
    def __init__(self):
        self.root = Tk()
        self.root.title('Department')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        branch_num = self.dept_num_e.get()
        self.branch_num_e.delete(0, END)
        branch_name = self.branch_name_e.get()
        self.branch_name_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO DEPARTMENT VALUES (" + branch_num + ",\"" + branch_name + "\")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.dept_num_lbl = Label(self.root, text='Department Num:')
        self.dept_num_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.dept_num_e = Entry(self.root, width=10, borderwidth=1)
        self.dept_num_e.grid(row=0, column=1, padx=5, pady=5)

        self.branch_name_lbl = Label(self.root, text='Department Name:')
        self.branch_name_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.branch_name_e = Entry(self.root, width=10, borderwidth=1)
        self.branch_name_e.grid(row=0, column=3, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Department()
    d.run()