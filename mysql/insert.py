import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="python_practise"
)

mycursor = mydb.cursor()
sql = "INSERT INTO customer (name,cnic,age) VALUES (%s,%s,%s)"
val = ("Musawer", 1234123123, 3)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record insert Successfully")

