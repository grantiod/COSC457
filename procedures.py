from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Procedures:
    def __init__(self):
        self.root = Tk()
        self.root.title('Procedures')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        procedure_num = self.procedure_num_e.get()
        self.procedure_num_e.delete(0, END)
        procedure_type = self.procedure_type_e.get()
        self.procedure_type_e.delete(0, END)
        procedure_criteria = self.procedure_criteria_e.get()
        self.procedure_criteria_e.delete(0, END)
        branch_num = self.branch_num_e.get()
        self.branch_num_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO PROCEDURES VALUES (" + procedure_num + ",\"" + procedure_type + "\",\"" + procedure_criteria + "\"," + branch_num + "\")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.procedure_num_lbl = Label(self.root, text='Procedure Num:')
        self.procedure_num_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.procedure_num_e = Entry(self.root, width=10, borderwidth=1)
        self.procedure_num_e.grid(row=0, column=1, padx=5, pady=5)

        self.procedure_type_lbl = Label(self.root, text='Procedure Type:')
        self.procedure_type_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.procedure_type_e = Entry(self.root, width=10, borderwidth=1)
        self.procedure_type_e.grid(row=0, column=3, padx=5, pady=5)

        self.procedure_criteria_lbl = Label(self.root, text='Procedure Criteria:')
        self.procedure_criteria_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.procedure_criteria_e = Entry(self.root, width=10, borderwidth=1)
        self.procedure_criteria_e.grid(row=0, column=5, padx=5, pady=5)

        self.branch_num_lbl = Label(self.root, text='Branch Num:')
        self.branch_num_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.branch_num_e = Entry(self.root, width=10, borderwidth=1)
        self.branch_num_e.grid(row=0, column=7, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    p = Procedures()
    p.run()