# creates the database and tables. Unused hereafter

import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="Gman1212!"
)

c = db.cursor()

# c.execute("SHOW DATABASES")

# c.execute("CREATE DATABASE psych_office")

c.execute("USE psych_office")

c.execute("SET FOREIGN_KEY_CHECKS = 0")

c.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE (employee_name VARCHAR(20), employee_num INT, ssn INT, dob DATE, address VARCHAR(20), PRIMARY KEY (employee_name, employee_num, ssn))")

# c.execute("INSERT INTO EMPLOYEE_HEALTH_INSURANCE VALUES (\"Grant Iodice\", 1234, \"Thomas\", \"BC Shield\")")

print(c.execute("SELECT * FROM EMPLOYEE_HEALTH_INSURANCE"))

db.close()