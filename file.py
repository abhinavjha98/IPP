import csv
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='ipp')

print('database connected')
cursor=mydb.cursor()


row=[int(id1),nc,month,sv,int(unit),int(iv),float(ipp)]
cur1.execute('INSERT INTO ipp_company (Company_ID,Name_of_Company,Months,Services,Unit,Invoice_Value,IPP) VALUES (%s,%s,%s,%s,%s,%s,%s)',row)   
mysql.connection.commit()

data = cursor.fetchall()
print(type(data))
print(data)


mydb.commit()
cursor.close()
