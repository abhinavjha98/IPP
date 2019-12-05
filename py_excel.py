import csv
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='ipp')
data1=""
data =['Sr.No','Name_of_Company','Company_ID','Services','Model','Unit','Invoice Value']

print('database connected')

cursor=mydb.cursor()

cursor.execute("SELECT * FROM services_invoice WHERE Company_ID = %s",(1001,))
data1=cursor.fetchall()
df = pd.DataFrame(data1,columns=['Sr.No','Name_of_Company','Company_ID','Month','Services','Model','Unit','Invoice Value'])
df.to_csv('Final.csv',index=False)
