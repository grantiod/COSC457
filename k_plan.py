from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class K_Plan:
    def __init__(self):
        self.root = Tk()
        self.root.title('401(k) Plan')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        account_num = self.account_num_e.get()
        self.account_num_e.delete(0, END)
        inv_per = self.invest_percentage_e.get()
        self.invest_percentage_e.delete(0, END)
        em_con_per = self.em_con_percentage_e.get()
        self.em_con_percentage_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)
        branch = self.branch_e.get()
        self.branch_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office_DB')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO FOUR_O_ONE_K_PLAN VALUES (" + account_num + "," + inv_per + "," + em_con_per + "," + employee_num + "," + branch + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.account_num_lbl = Label(self.root, text='Account Num:')
        self.account_num_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.account_num_e = Entry(self.root, width=10, borderwidth=1)
        self.account_num_e.grid(row=0, column=1, padx=5, pady=5)

        self.invest_percentage_lbl = Label(self.root, text='Investment Percentage:')
        self.invest_percentage_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.invest_percentage_e = Entry(self.root, width=10, borderwidth=1)
        self.invest_percentage_e.grid(row=0, column=3, padx=5, pady=5)

        self.em_con_percentage_lbl = Label(self.root, text='Employer Contribution Percentage:')
        self.em_con_percentage_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.em_con_percentage_e = Entry(self.root, width=10, borderwidth=1)
        self.em_con_percentage_e.grid(row=0, column=5, padx=5, pady=5)

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
    k = K_Plan()
    k.run()