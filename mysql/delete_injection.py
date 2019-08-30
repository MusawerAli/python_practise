import mysql.connector

import db
mydb = db.db_connection("localhost","root","root","python_practise")

mycursor = mydb.cursor()
sql = "DELETE from customer where id = %s"
del_id = (31,)

mycursor.execute(sql, del_id)
mydb.commit()
print(mycursor.rowcount, "Record Deleted Successfully")