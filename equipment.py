from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Equipment:
    def __init__(self):
        self.root = Tk()
        self.root.title('Equipment')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        asset_id = self.asset_id_e.get()
        self.asset_id_e.delete(0, END)
        estimated_value = self.estimated_value_e.get()
        self.estimated_value_e.delete(0, END)
        contact_on_file = self.contact_on_file_e.get()
        self.contact_on_file_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)
        branch = self.branch_e.get()
        self.branch_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO EQUIPMENT VALUES (" + asset_id + "," + estimated_value + ",\"" + contact_on_file + "\"," + employee_num + "," + branch + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.asset_id_lbl = Label(self.root, text='Asset ID:')
        self.asset_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.asset_id_e = Entry(self.root, width=10, borderwidth=1)
        self.asset_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.estimated_value_lbl = Label(self.root, text='Estimated Value:')
        self.estimated_value_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.estimated_value_e = Entry(self.root, width=10, borderwidth=1)
        self.estimated_value_e.grid(row=0, column=3, padx=5, pady=5)

        self.contact_on_file_lbl = Label(self.root, text='Contact On File:')
        self.contact_on_file_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.contact_on_file_e = Entry(self.root, width=10, borderwidth=1)
        self.contact_on_file_e.grid(row=0, column=5, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee ID:')
        self.employee_num_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=7, padx=5, pady=5)

        self.branch_lbl = Label(self.root, text='Branch Num:')
        self.branch_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.branch_e = Entry(self.root, width=10, borderwidth=1)
        self.branch_e.grid(row=0, column=9, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    e = Equipment()
    e.run()