import csv
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='ipp')
data1=""
data =['Sr.No','Name_of_Company','Company_ID','Services','Model','Unit','Invoice Value']

print('database connected')

cursor=mydb.cursor()

cursor.execute("SELECT * FROM ipp_company")
data1=cursor.fetchall()
df = pd.DataFrame(data1,columns=['Company_ID','Name_of_Company','Months','Services','Unit','Invoice_Value','IPP'])
df.to_csv('Final_invoice.csv',index=False)
