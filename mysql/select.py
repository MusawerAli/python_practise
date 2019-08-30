import mysql.connector
import db
mydb = db.db_connection("localhost","root","root","python_practise")
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="root",
#     database="python_practise"
# )
mycursor = mydb.cursor()

mycursor.execute("SELECT * from customer")

myresult = mycursor.fetchall()
mySingleResult = mycursor.fetchone()
for x in myresult:
    print(x)


print(mySingleResult)
