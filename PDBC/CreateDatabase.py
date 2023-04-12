'''import mysql.connector
demodb=mysql.connector.connect(host="localhost", user="root", passwd="tiger")
democursor=demodb.cursor()
democursor.execute("create database new")
demodb.close()'''

import mysql.connector
db=mysql.connector.connect(host="localhost", user="root", passwd="tiger")
cursor=db.cursor()
cursor.execute("create database anupacc")
cursor.close()
db.close()

                    
