import mysql.connector

import db
mydb = db.db_connection("localhost","root","root","python_practise")

mycursor = mydb.cursor()

sql = "SELECT * FROM customer where name = %s"
name = ("Musawer",)
mycursor.execute(sql, name)

result = mycursor.fetchall()

for x in result:
    print(x)