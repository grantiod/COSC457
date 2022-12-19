from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Service:
    def __init__(self):
        self.root = Tk()
        self.root.title('Service')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        num = self.num_e.get()
        self.num_e.delete(0, END)
        name = self.name_e.get()
        self.name_e.delete(0, END)
        rate = self.rate_e.get()
        self.rate_e.delete(0, END)
        dept_num = self.dept_num_e.get()
        self.dept_num_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO SERVICE VALUES (" + num + ",\"" + name + "\"," + rate + ",\"" + dept_num + "\")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.num_lbl = Label(self.root, text='Service Num:')
        self.num_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.num_e = Entry(self.root, width=10, borderwidth=1)
        self.num_e.grid(row=0, column=1, padx=5, pady=5)

        self.name_lbl = Label(self.root, text='Service Name:')
        self.name_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.name_e = Entry(self.root, width=10, borderwidth=1)
        self.name_e.grid(row=0, column=3, padx=5, pady=5)

        self.rate_lbl = Label(self.root, text='Rate:')
        self.rate_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.rate_e = Entry(self.root, width=10, borderwidth=1)
        self.rate_e.grid(row=0, column=5, padx=5, pady=5)

        self.dept_num_lbl = Label(self.root, text='Department Num:')
        self.dept_num_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.dept_num_e = Entry(self.root, width=10, borderwidth=1)
        self.dept_num_e.grid(row=0, column=7, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    o = Service()
    o.run()