import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="python_practise"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customer (name,cnic,age) values(%s,%s,%s)"
values = [
    ('ALi',5345,34),
    ('ALi Reh',5345,66),
    ('Pixel',4347546,23),
    ('Micel',235463,54),
    ('Peter',785463,65),
    ('Nxae',7345345,76)

]


mycursor.executemany(sql, values)
mydb.commit()
print(mycursor.rowcount, "Was Inserted")
print("last insert row id is: ", mycursor.lastrowid)