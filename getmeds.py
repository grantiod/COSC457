from tkinter import Entry, Button, Tk, END, mainloop, Label, Toplevel
import MySQLdb

class Get_Meds:
    def __init__(self):
        self.root = Tk()
        self.root.title('Get Meds')

    # upload data to db
    def submit(self):
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Gman1212!"
        )

        c = db.cursor()
        c.execute('USE psych_office_DB')

        patient_id = self.patient_e.get()

        try:
            toplevel = Toplevel()
            c.execute("select m.med_id, med_name, pe.Fname, pe.Lname from medication m inner join prescription p on p.med_id = m.med_id inner join patient pa on pa.patient_id = p.patient_id inner join person pe on pe.ssn = pa.ssn where " + patient_id + " = pa.patient_id")
            output = c.fetchall()
            w = 0
            for x in output:
                output_lbl = Label(toplevel, text=w)
                output_lbl.grid(row=2, column=0, padx=5, pady=5)
        except:
            pass

        db.commit()
        c.close()
        db.close()

    def run(self):
        self.patient_lbl = Label(self.root, text='Patient ID:')
        self.patient_lbl.grid(row=0, column=0, padx=5, pady=5)
        self.patient_e = Entry(self.root, width=10, borderwidth=1)
        self.patient_e.grid(row=0, column=1, padx=5, pady=5)

        self.submit = Button(self.root, text='Submit', padx=5, pady=5, command=self.submit)
        self.submit.grid(row=1, column=0)

        mainloop()

if __name__ == '__main__':
    d = Get_Meds()
    d.run()