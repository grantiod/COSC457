# creates the database and tables. Unused hereafter

import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="password"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXIST psych_office")

db.close()