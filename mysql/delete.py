import mysql.connector

import db
mydb = db.db_connection("localhost","root","root","python_practise")

mycursor = mydb.cursor()

sql = "DELETE from customer where id = 23"

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"Record deleted successfully")