import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sreehari@2001",
  database="student"
)


cursor=db.cursor()

query = "SELECT project.Rollno,project.Name,project.Email,project.Qualification,project.Skill,company.Company FROM project INNER JOIN company ON project.Rollno=company.Rollno"
cursor.execute(query)
rows=cursor.fetchall()
for x in rows:
   print(x)

db.close()