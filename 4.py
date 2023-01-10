
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sreehari@2001",
        database="student"
    )
mycursor = mydb.cursor()

sql = "DROP TABLE project"

mycursor.execute(sql)