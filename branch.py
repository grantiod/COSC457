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

        c = db.cursor()
        c.execute('USE psych_office')
        c.close()

    def run(self):
        self.branch_num_lbl = Label(self.root, text='Branch Num:')
        self.branch_num_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.branch_num_e = Entry(self.root, width=10, borderwidth=1)
        self.branch_num_e.grid(row=0, column=1, padx=5, pady=5)

        self.branch_name_lbl = Label(self.root, text='Branch Name:')
        self.branch_name_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.branch_name_e = Entry(self.root, width=10, borderwidth=1)
        self.branch_name_e.grid(row=0, column=3, padx=5, pady=5)

        self.state_lbl = Label(self.root, text='State:')
        self.state_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.state_e = Entry(self.root, width=10, borderwidth=1)
        self.state_e.grid(row=0, column=5, padx=5, pady=5)

        self.address_lbl = Label(self.root, text='Address:')
        self.address_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.address_e = Entry(self.root, width=10, borderwidth=1)
        self.address_e.grid(row=0, column=7, padx=5, pady=5)

        self.contact_lbl = Label(self.root, text='Contact:')
        self.contact_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.contact_e = Entry(self.root, width=10, borderwidth=1)
        self.contact_e.grid(row=0, column=9, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Branch()
    d.run()