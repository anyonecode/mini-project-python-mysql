rollno = int( input('enter your rollno : '))
name = input('enter your name : ')
email = input('enter your email : ')
qualification = input('enter qualification [diploma,btech,degree,master degree,other] : ')
skill = input('enter skill : ')
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sreehari@2001",
        database="student"
    )

mycursor = mydb.cursor()

sql = "INSERT INTO project (Rollno,Name,Email,Qualification,Skill) VALUES (%s,%s, %s,%s,%s)"
val = (rollno,name, email, qualification, skill)
mycursor.execute(sql, val)

mydb.commit()
if qualification == 'btech':
    print('the company you can apply: ''1.tcs',
              '2.wipro',
              '3.infosys',
              '4.l&t',
              '5.ibm',
              '6.mindtree')
elif qualification == 'diploma':
    print('the company you can apply: ''1.Tata motors',
              '2.CTS',
              '3.Hexaware',
              '4.HCL Technologies',
              '5.Reliance',
              '6.SFO')
elif qualification == 'degree':
    print('the company you can apply: ''1.Goldman Sachs',
              '2.Amazon',
              '3.Capital One',
              '4.Prudential Financial',
              '5.AT&T',
              '6.Cigna')
elif qualification == 'master degree':
    print('the company you can apply: ''1.Google',
              '2.PRH',
              '3.CW',
              '4.Whole Foods',
              '5.Hilton',
              '6.Publix')
else:
    print('the company you can apply: ''1.Swiggy',
              '2.Zomato',
              '3.indian oil',
              '4.bharat petroleum',
              '5.newone',
              '6.AB solutions')
y_n = input('application conformation y/n : ')
if y_n == "y":
    print('thank you for applying')
if y_n=='n':
    import mysql.connector
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sreehari@2001",
            database="student"
        )

    mycursor = mydb.cursor()

    sql = "DELETE FROM project WHERE Name = %s "
    adr = (name,)

    mycursor.execute(sql,adr)

    mydb.commit()
    print('the application canceled')
    exit()


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
adr = (Company,)

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for y in myresult:
    print('company and their vacancy',y)
    print('thank you for applying')

import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sreehari@2001",
        database="student"
    )

mycursor = mydb.cursor()

sql = "INSERT INTO company (Company,Rollno) VALUES (%s,%s)"
val = (Company,rollno)
mycursor.execute(sql, val)

mydb.commit()

import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sreehari@2001",
        database="student"
    )

cursor = db.cursor()

query = "SELECT project.Rollno,project.Name,project.Email,project.Qualification,project.Skill,company.Company FROM project INNER JOIN company ON project.Rollno=company.Rollno"
cursor.execute(query)
rows = cursor.fetchall()
for x in rows:
    print(x)







