cursor.execute('INSERT INTO company_master (Name_of_Company,Company_ID,Supervisor,Services,Service_Charges,Actual_Stipend,Working_Condition,Facilities,others) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
cursor.execute('INSERT INTO employee_masters (Name,Emp_No,Level,Direct_Indirect,Company) VALUES (%s,%s,%s,%s,%s,%s)',row)