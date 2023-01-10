# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="sreehari@2001",
#   database="vacacy"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE TABLE no_vacancy (company VARCHAR(255), vacancy int(255))")
# print('the company you can apply: ''1.Goldman Sachs',
#         '2.Amazon',
#         '3.Capital One',
#         '4.Prudential Financial',
#         '5.AT&T',
#         '6.Cigna')

Company = input('which company you want to apply : ')
'''selecting second database'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sreehari@2001",
  database="vacacy"
)
mycursor = mydb.cursor()

sql = "SELECT * FROM no_vacancy WHERE company = %s"
adr = (Company, )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for y in myresult:
  print()
y_n = input('application conformation y/n : ')
if y_n == "y":
  print('thank you for applying')
else:
  print('the application canceled')