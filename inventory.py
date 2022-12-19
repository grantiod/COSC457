from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Inventory:
    def __init__(self):
        self.root = Tk()
        self.root.title('Inventory')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        items = self.items_e.get()
        self.items_e.delete(0, END)
        stock = self.stock_e.get()
        self.stock_e.delete(0, END)
        supplier_address = self.supplier_address_e.get()
        self.supplier_address_e.delete(0, END)
        branch_num = self.branch_num_e.get()
        self.branch_num_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute('INSERT INTO INVENTORY VALUES (\"' + items + "\"," + stock + ",\"" + supplier_address + "\"," + branch_num + ')')
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.items_lbl = Label(self.root, text='Items:')
        self.items_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.items_e = Entry(self.root, width=10, borderwidth=1)
        self.items_e.grid(row=0, column=1, padx=5, pady=5)

        self.stock_lbl = Label(self.root, text='Stock:')
        self.stock_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.stock_e = Entry(self.root, width=10, borderwidth=1)
        self.stock_e.grid(row=0, column=3, padx=5, pady=5)

        self.supplier_address_lbl = Label(self.root, text='Supplier:')
        self.supplier_address_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.supplier_address_e = Entry(self.root, width=10, borderwidth=1)
        self.supplier_address_e.grid(row=0, column=5, padx=5, pady=5)

        self.branch_num_lbl = Label(self.root, text='Branch Num:')
        self.branch_num_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.branch_num_e = Entry(self.root, width=10, borderwidth=1)
        self.branch_num_e.grid(row=0, column=7, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    i = Inventory()
    i.run()