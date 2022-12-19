from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Office_Bill:
    def __init__(self):
        self.root = Tk()
        self.root.title('Office Bill')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        bill_num = self.bill_num_e.get()
        self.bill_num_e.delete(0, END)
        branch_num = self.branch_num_e.get()
        self.branch_num_e.delete(0, END)
        issue_date = self.issue_date_e.get()
        self.issue_date_e.delete(0, END)
        issuer = self.issuer_e.get()
        self.issuer_e.delete(0, END)
        payment_date = self.payment_date_e.get()
        self.payment_date_e.delete(0, END)
        charge = self.charge_e.get()
        self.charge_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO OFFICE_BILL VALUES (" + bill_num + "," + branch_num + ",\"" + issue_date + "\",\"" + issuer + "\",\"" + payment_date + "\"," + charge + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.bill_num_lbl = Label(self.root, text='Bill Num:')
        self.bill_num_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.bill_num_e = Entry(self.root, width=10, borderwidth=1)
        self.bill_num_e.grid(row=0, column=1, padx=5, pady=5)

        self.branch_num_lbl = Label(self.root, text='Branch Num:')
        self.branch_num_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.branch_num_e = Entry(self.root, width=10, borderwidth=1)
        self.branch_num_e.grid(row=0, column=3, padx=5, pady=5)

        self.issue_date_lbl = Label(self.root, text='Issue Date:')
        self.issue_date_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.issue_date_e = Entry(self.root, width=10, borderwidth=1)
        self.issue_date_e.grid(row=0, column=5, padx=5, pady=5)

        self.issuer_lbl = Label(self.root, text='Issuer:')
        self.issuer_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.issuer_e = Entry(self.root, width=10, borderwidth=1)
        self.issuer_e.grid(row=0, column=7, padx=5, pady=5)

        self.payment_date_lbl = Label(self.root, text='Payment Date:')
        self.payment_date_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.payment_date_e = Entry(self.root, width=10, borderwidth=1)
        self.payment_date_e.grid(row=0, column=9, padx=5, pady=5)

        self.charge_lbl = Label(self.root, text='Charge:')
        self.charge_lbl.grid(row=0, column=10, padx=5, pady=5)
        self.charge_e = Entry(self.root, width=10, borderwidth=1)
        self.charge_e.grid(row=0, column=11, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    o = Office_Bill()
    o.run()