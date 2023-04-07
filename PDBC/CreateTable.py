import mysql.connector
db=mysql.connector.connect(host="localhost", user="root", passwd="tiger", database="new")
cursor=db.cursor()
cursor.execute("create table student(rollno int primary key, name varchar(50), class int, marks int)")
cursor.execute("desc student")
for i in cursor:
    print(i)
db.close()
