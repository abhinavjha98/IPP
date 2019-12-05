import csv
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='ipp')
data1=""
data =['Sr.No','Name_of_Company','Company_ID','Services','Model','Unit','Invoice Value']

print('database connected')

cursor=mydb.cursor()

cursor.execute("SELECT * FROM employee_master ")
data1=cursor.fetchall()
df = pd.DataFrame(data1,columns=['Sr_No','Prepared_By','Code','Emp_No','Name','Gender','Father_Name','DOB','DOJ','Paid_By','Cost_Centre','Employee_Name_On_Passbook','Bank_Name','Branch_Name','IFSC_Code','Beneficiary_Account_Number','Beneficiary_City','State','email_address','pay_days','total_days','location','Bank_State','CPI_eligibility','Designation','ODOJ','Level','Direct_Indirect','Reporting_1','Reporting_2','Reporting_3','Reporting_4','Reporting_5','Personal_Official_No','Company'])
df.to_csv('Final_emp.csv',index=False)
