import csv
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='ipp')

print('database connected')

cursor=mydb.cursor()
csv_data = csv.reader(open('E:/PROJECT/ipp/uploads/samples.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO dod_table (reputation_client,training_fee,stipend,working_condition,transport_canteen_facility,others) VALUES (%s,%s,%s,%s,%s,%s)',row)
    print(type(row[0]))
mydb.commit()
cursor.close()
