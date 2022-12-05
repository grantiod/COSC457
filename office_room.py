from tkinter import Entry, Button, Tk, END, mainloop, Label
import MySQLdb

class Office_Room:
    def __init__(self):
        self.root = Tk()
        self.root.title('Office Room')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        room_id = self.room_id_e.get()
        self.room_id_e.delete(0, END)
        address = self.address_e.get()
        self.address_e.delete(0, END)
        room_num = self.room_num_e.get()
        self.room_num_e.delete(0, END)
        employee_num = self.employee_num_e.get()
        self.employee_num_e.delete(0, END)

        c = db.cursor()
        c.execute('USE psych_office')
        c.execute('SET FOREIGN_KEY_CHECKS = 0')
        c.execute("INSERT INTO OFFICE_ROOMS VALUES (" + room_id + ",\"" + address + "\"," + room_num + "," + employee_num + ")")
        c.execute('SET FOREIGN_KEY_CHECKS = 1')
        db.commit()
        c.close()
        db.close()

    def run(self):
        self.room_id_lbl = Label(self.root, text='Room ID:')
        self.room_id_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.room_id_e = Entry(self.root, width=10, borderwidth=1)
        self.room_id_e.grid(row=0, column=1, padx=5, pady=5)

        self.address_lbl = Label(self.root, text='Address:')
        self.address_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.address_e = Entry(self.root, width=10, borderwidth=1)
        self.address_e.grid(row=0, column=3, padx=5, pady=5)

        self.room_num_lbl = Label(self.root, text='Room Number:')
        self.room_num_lbl.grid(row=0, column=4, padx=5, pady=5)
        self.room_num_e = Entry(self.root, width=10, borderwidth=1)
        self.room_num_e.grid(row=0, column=5, padx=5, pady=5)

        self.employee_num_lbl = Label(self.root, text='Employee Number:')
        self.employee_num_lbl.grid(row=0, column=6, padx=5, pady=5)
        self.employee_num_e = Entry(self.root, width=10, borderwidth=1)
        self.employee_num_e.grid(row=0, column=7, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    o = Office_Room()
    o.run()