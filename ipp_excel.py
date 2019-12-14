import csv
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='ipp')
data1=""
data =['Company_ID','Name_of_Company','Unit','IPP']

print('database connected')

cursor=mydb.cursor()

cursor.execute("SELECT Company_ID,Name_of_Company,Unit,IPP FROM ipp_company")
data1=cursor.fetchall()
df = pd.DataFrame(data1,columns=['Company_ID','Name_of_Company','Unit','IPP'])
df.drop_duplicates(subset ="Name_of_Company", 
                     keep = "first", inplace = True) 
df.to_csv('Final_ipp.csv',index=False)
