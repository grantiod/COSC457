from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Business_Accounts:
    def __init__(self):
        self.root = Tk()
        self.root.title('Business Accounts')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        account_id = self.account_id_e.get()
        self.account_id_e.delete(0, END)
        company_name = self.company_name_e.get()
        self.company_name_e.delete(0, END)
        contact = self.contact_e.get()
        self.contact_e.delete(0, END)
        address = self.address_e.get()
        self.address_e.delete(0, END)
        service = self.service_e.get()
        self.service_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO BUSINESS_ACCOUNTS VALUES (" + account_id + ",\"" + company_name + "\",\"" + contact + "\",\"" + address + "\",\"" + service + "\")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.account_id_lbl = Label(self.root, text='Account ID:')
        self.account_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.account_id_e = Entry(self.root, width=10, borderwidth=1)
        self.account_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.company_name_lbl = Label(self.root, text='Company Name:')
        self.company_name_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.company_name_e = Entry(self.root, width=10, borderwidth=1)
        self.company_name_e.grid(row=0, column=3, padx=5, pady=5)

        self.contact_lbl = Label(self.root, text='Contact:')
        self.contact_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.contact_e = Entry(self.root, width=10, borderwidth=1)
        self.contact_e.grid(row=0, column=5, padx=5, pady=5)

        self.address_lbl = Label(self.root, text='Address:')
        self.address_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.address_e = Entry(self.root, width=10, borderwidth=1)
        self.address_e.grid(row=0, column=7, padx=5, pady=5)

        self.service_lbl = Label(self.root, text='Service:')
        self.service_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.service_e = Entry(self.root, width=10, borderwidth=1)
        self.service_e.grid(row=0, column=9, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    b = Business_Accounts()
    b.run()