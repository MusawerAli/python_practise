import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE python_practise")

print("Created Successfully") if mycursor else print("Some Error")