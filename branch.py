from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Branch:
    def __init__(self):
        self.root = Tk()
        self.root.title('Branch')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        branch_num = self.branch_num_e.get()
        self.branch_num_e.delete(0, END)
        branch_name = self.branch_name_e.get()
        self.branch_name_e.delete(0, END)
        street = self.street_e.get()
        self.street_e.delete(0, END)
        city = self.city_e.get()
        self.city_e.delete(0, END)
        state = self.state_e.get()
        self.state_e.delete(0, END)
        contact = self.contact_e.get()
        self.contact_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO BRANCH VALUES (" + branch_num + ",\"" + branch_name + "\",\"" + street + "\",\"" + city + "\",\"" + state + "\"," + contact + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.branch_num_lbl = Label(self.root, text='Branch Num:')
        self.branch_num_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.branch_num_e = Entry(self.root, width=10, borderwidth=1)
        self.branch_num_e.grid(row=0, column=1, padx=5, pady=5)

        self.branch_name_lbl = Label(self.root, text='Branch Name:')
        self.branch_name_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.branch_name_e = Entry(self.root, width=10, borderwidth=1)
        self.branch_name_e.grid(row=0, column=3, padx=5, pady=5)

        self.street_lbl = Label(self.root, text='Street:')
        self.street_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.street_e = Entry(self.root, width=10, borderwidth=1)
        self.street_e.grid(row=0, column=5, padx=5, pady=5)

        self.city_lbl = Label(self.root, text='City:')
        self.city_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.city_e = Entry(self.root, width=10, borderwidth=1)
        self.city_e.grid(row=0, column=7, padx=5, pady=5)

        self.state_lbl = Label(self.root, text='State:')
        self.state_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.state_e = Entry(self.root, width=10, borderwidth=1)
        self.state_e.grid(row=0, column=9, padx=5, pady=5)

        self.contact_lbl = Label(self.root, text='Phone:')
        self.contact_lbl.grid(row=0, column=10, padx=5, pady=5)
        self.contact_e = Entry(self.root, width=10, borderwidth=1)
        self.contact_e.grid(row=0, column=11, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Branch()
    d.run()