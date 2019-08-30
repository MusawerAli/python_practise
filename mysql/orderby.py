import mysql.connector

import db
mydb = db.db_connection("localhost","root","root","python_practise")

mycursor = mydb.cursor()

sql = "SELECT * from customer order by id DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)