#program to create a table, insert data, and display data

import mysql.connector
db=mysql.connector.connect(host="localhost", user="root", passwd="tiger", database="anupacc")
cursor=db.cursor()
'''cursor.execute("create table employee1(empno int(5) primary key, empname varchar(50), sal double, addr varchar(50))")
print("table created")'''

cursor.execute("INSERT INTO employee1 (empno, empname, sal, addr) VALUES(%s, %s, %s, %s)".format(104, 'Kopal',10800, 'Lucknow'))
               
print("values inserted successfully")

data=cursor.fetchall()
for row in data:
    print (row)
    
db.commit()    
cursor.close()
db.close()
               
