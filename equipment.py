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

        c = db.cursor()
        c.execute('USE psych_office')
        c.close()

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

        self.employee_num_lbl = Label(self.root, text='Employee Num:')
        self.employee_num_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=7, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    e = Equipment()
    e.run()