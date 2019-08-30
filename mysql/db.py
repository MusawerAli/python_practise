import mysql.connector


def db_connection(dbhost, user, pwd, db):
    mydb = mysql.connector.connect(
        host=dbhost,
        user=user,
        passwd=pwd,
        database=db 
    )

    return mydb
    