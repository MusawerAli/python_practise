import mysql.connector

import db
mydb = db.db_connection("localhost","root","root","python_practise")

mycursor = mydb.cursor()

sql = "UPDATE customer set name = %s where name = %s"
injection = ('Musawer', 'ALi')

mycursor.execute(sql, injection)

mydb.commit()

print(mycursor.rowcount, "Record updated successfully")
