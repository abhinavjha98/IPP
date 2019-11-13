import csv
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='ipp')

print('database connected')

cursor=mydb.cursor()
csv_data = csv.reader(open('E:/PROJECT/ipp/uploads/sample1.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO company_master_table (Sr_No,Name_of_Company,Company_ID,Unit,Address,State,PinCode,Customer_Contact_Person,Customer_Contact_Number,Supervisor,Reporting_1,Reporting_2,Reporting_3,Reporting_4,Reporting_5,Closed_By,Services_A,Services_Model,Reputation_of_client,Service_Charges,Actual_Stipend,Working_Condition,Facilities) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
mydb.commit()
cursor.close()
