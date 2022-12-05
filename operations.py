from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Operations:
    def __init__(self):
        self.root = Tk()
        self.root.title('Operations')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        operation_type = self.operation_type_e.get()
        self.operation_type_e.delete(0, END)
        patient_id = self.patient_id_e.get()
        self.patient_id_e.delete(0, END)
        operation_date = self.operation_date_e.get()
        self.operation_date_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)
        operation_cost = self.operation_cost_e.get()
        self.operation_cost_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO OPERATIONS VALUES (\"" + operation_type + "\"," + patient_id + ",\"" + operation_date + "\"," + employee_num + "," + operation_cost + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.operation_type_lbl = Label(self.root, text='Operation Type:')
        self.operation_type_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.operation_type_e = Entry(self.root, width=10, borderwidth=1)
        self.operation_type_e.grid(row=0, column=1, padx=5, pady=5)

        self.patient_id_lbl = Label(self.root, text='Patient ID:')
        self.patient_id_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.patient_id_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_id_e.grid(row=0, column=3, padx=5, pady=5)

        self.operation_date_lbl = Label(self.root, text='Operation Date:')
        self.operation_date_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.operation_date_e = Entry(self.root, width=10, borderwidth=1)
        self.operation_date_e.grid(row=0, column=5, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee Num:')
        self.employee_num_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=7, padx=5, pady=5)

        self.operation_cost_lbl = Label(self.root, text='Operation Cost:')
        self.operation_cost_lbl.grid(row=0, column=8, padx=5, pady=5)
        self.operation_cost_e = Entry(self.root, width=10, borderwidth=1)
        self.operation_cost_e.grid(row=0, column=9, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    o = Operations()
    o.run()