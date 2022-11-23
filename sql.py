from tkinter import Entry, Tk, END, mainloop, Button
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
        query = self.entry.get()
        self.entry.delete(0, END)

        query = query.lower()

        if query[0:5] == 'select':
            pass

if __name__ == '__main__':
    s = SQL()
    s.run()