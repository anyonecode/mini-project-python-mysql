import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sreehari@2001",
  database="student"
)



mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE project (Rollno INT PRIMARY KEY, Name VARCHAR(255), Email VARCHAR(255), Qualification VARCHAR(255), Skill VARCHAR(255))")

