from tkinter import Entry, Tk, END, mainloop, Text, Button
import MySQLdb

class SQL:
    def __init__(self):
        self.root = Tk()
        self.root.title('SQL')

    def run(self):
        self.entry = Text(self.root, width=50, height=10)
        self.entry.grid(row=0, column=0, padx=5, pady=5)
        self.submit_btn = Button(self.root, text="Submit", command=self.submit)
        self.submit_btn.grid(row=1, column=0, padx=5, pady=5)

        mainloop()

    # implement output for select queries
    def submit(self):
        query = self.entry.get()
        self.entry.delete(0, END)

if __name__ == '__main__':
    s = SQL()
    s.run()