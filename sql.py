from tkinter import Entry, Tk, mainloop, Button, Label, Toplevel
import MySQLdb

class SQL:
    def __init__(self):
        self.root = Tk()
        self.root.title('SQL')

    def run(self):
        self.entry = Entry(self.root, width=50)
        self.entry.grid(row=0, column=0, padx=5, pady=5)
        self.submit_btn = Button(self.root, text="Submit", command=self.submit)
        self.submit_btn.grid(row=1, column=0, padx=5, pady=5)

        mainloop()

    # implement output for select queries
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        c = db.cursor()
        c.execute('USE psych_office_DB')

        query = self.entry.get()
        # self.entry.delete(0, END)

        query = query.upper()
        # print(query)

        if query[0:6] == 'SELECT':
            toplevel = Toplevel(self.root)

            try:
                c.execute(query)
                output = c.fetchall()
                w = 0
                for x in output:
                    output_lbl = Label(toplevel, text=x)
                    output_lbl.grid(row=w, column=0, padx=5, pady=5)
                    w += 1
            except:
                pass
        else:
            pass

        db.commit()
        c.close()
        db.close()

if __name__ == '__main__':
    s = SQL()
    s.run()