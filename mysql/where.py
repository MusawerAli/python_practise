import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="python_practise"
)

mycursor = mydb.cursor()

sql = "SELECT * from customer where name = 'Musawer'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)