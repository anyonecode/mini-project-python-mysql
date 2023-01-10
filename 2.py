import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sreehari@2001",
  database="student"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)
#   import mysql.connector
#
#   mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="sreehari@2001",
#     database="student"
#   )
#
#   mycursor = mydb.cursor()
#
#   mycursor.execute("select count(*) from project")