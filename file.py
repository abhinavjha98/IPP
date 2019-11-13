import csv
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='ipp')

print('database connected')
cursor=mydb.cursor()

cursor.execute("SELECT * FROM company_master_table WHERE Unit= %s", (78,))

data = cursor.fetchall()
print(type(data))
print(data)


mydb.commit()
cursor.close()
