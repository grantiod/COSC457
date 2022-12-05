from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Pharmacy:
    def __init__(self):
        self.root = Tk()
        self.root.title('Pharmacy')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        pharmacy_id = self.pharmacy_id_e.get()
        self.pharmacy_id_e.delete(0, END)
        pharmacy_name = self.pharmacy_name_e.get()
        self.pharmacy_name_e.delete(0, END)
        owner = self.owner_e.get()
        self.owner_e.delete(0, END)
        contact = self.contact_e.get()
        self.contact_e.delete(0, END)
        address = self.address_e.get()
        self.address_e.delete(0, END)
        medication_id = self.medication_id_e.get()
        self.medication_id_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO PHARMACY VALUES (" + pharmacy_id + ",\"" + pharmacy_name + "\",\"" + owner + "\",\"" + contact + "\",\"" + address + "\"," + medication_id + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.pharmacy_id_lbl = Label(self.root, text='Pharmacy ID:')
        self.pharmacy_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.pharmacy_id_e = Entry(self.root, width=10, borderwidth=1)
        self.pharmacy_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.pharmacy_name_lbl = Label(self.root, text='Pharmacy Name:')
        self.pharmacy_name_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.pharmacy_name_e = Entry(self.root, width=10, borderwidth=1)
        self.pharmacy_name_e.grid(row=0, column=3, padx=5, pady=5)

        self.owner_lbl = Label(self.root, text='Owner:')
        self.owner_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.owner_e = Entry(self.root, width=10, borderwidth=1)
        self.owner_e.grid(row=0, column=5, padx=5, pady=5)

        self.contact_lbl = Label(self.root, text='Contact:')
        self.contact_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.contact_e = Entry(self.root, width=10, borderwidth=1)
        self.contact_e.grid(row=0, column=7, padx=5, pady=5)

        self.address_lbl = Label(self.root, text='Address:')
        self.address_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.address_e = Entry(self.root, width=10, borderwidth=1)
        self.address_e.grid(row=0, column=9, padx=5, pady=5)

        self.medication_id_lbl = Label(self.root, text='Medicaiton ID:')
        self.medication_id_lbl.grid(row=0, column=10, padx=5, pady=5)
        self.medication_id_e = Entry(self.root, width=10, borderwidth=1)
        self.medication_id_e.grid(row=0, column=11, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    p = Pharmacy()
    p.run()