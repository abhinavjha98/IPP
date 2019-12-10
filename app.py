from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import os
from flask_wtf import Form
import urllib.request
from flask_wtf.file import FileField
import csv
import mysql.connector as ms
from werkzeug.utils import secure_filename
from flask import send_file
import pandas as pd
UPLOAD_FOLDER = 'E:/PROJECT/ipp/uploads'
app = Flask(__name__)

app.secret_key = 'many random bytes'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ipp'

mysql = MySQL(app)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','xlsx','csv'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():

    return render_template('index2.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method =='POST':
        if request.form['submit_button'] == 'register':
            FirstName = request.form['FirstName']
            LastName = request.form['LastName']
            emailid = request.form['emailid']
            password = request.form['password']
            cur1 = mysql.connection.cursor()
            cur1.execute('INSERT INTO registration (FirstName,LastName,emailid,password) VALUES (%s,%s,%s,%s)',(FirstName,LastName,emailid,password))
            mysql.connection.commit()
            return redirect(request.url)
        elif request.form['submit_button'] == 'login':
            emailid = request.form['emailid']
            password = request.form['password']
            cur1 = mysql.connection.cursor()
            a = cur1.execute('SELECT * FROM registration WHERE emailid=%s and password=%s',(emailid,password))
            if a == 1:
                flash("successfully")
                return render_template('index2.html')
            else:
                print("Please check your password")
                return render_template('login.html')
            mysql.connection.commit()
    return render_template('login.html')


@app.route('/uploads')
def upload_form():
	return render_template('uploads.html')

@app.route('/download',methods=['GET','POST'])
def download():
    if request.method == 'POST':
        mydb = ms.connect(host='localhost',user='root',password='',database='ipp')
        cursor=mydb.cursor()
        cursor.execute("SELECT * FROM services_invoice")
        data1=cursor.fetchall()
        df = pd.DataFrame(data1,columns=['Sr_No','Name_of_Company','Company_ID','Month','Services','Model','Unit','Invoice_Value'])
        df.to_csv('E:/PROJECT/ipp/static/Final.csv',index=False)
        path = "E:/PROJECT/ipp/static/Final.csv"
        return send_file(path,mimetype='text/csv' ,attachment_filename='Final.csv',as_attachment=True)
    return render_template('download.html')

@app.route('/reports',methods=['GET','POST'])
def reports():
    if request.method== 'POST':
        if request.form['submit_button']=='IPP':
            print("hello")
            mydb = ms.connect(host='localhost',user='root',password='',database='ipp')
            cursor=mydb.cursor()
            cursor1=mydb.cursor()
            cursor.execute("SELECT * FROM services_invoice")
            data3 = cursor.fetchall()
            data = pd.DataFrame(data3,columns=['Sr.No','Name_of_Company','Company_ID','Month','Services','Model','Unit','Invoice Value'])
            cursor1.execute("SELECT * FROM company_master_table")
            data2=cursor1.fetchall()
            data1 = pd.DataFrame(data2,columns=['Sr_No','Name_of_Company','Company_ID','Month','Unit','Address','State','PinCode','Customer_Contact_Person','Customer_Contact_Number','Supervisor','Reporting_1','Reporting_2','Reporting_3','Reporting_4','Reporting_5','Closed_By','Services_A','Services_Model','Reputation_of_client','Service_Charges','Actual_Stipend','Working_Condition','Facilities','others'])
            for i in data1.index:
                id1 = data1.get_value(i,'Company_ID')
                sc = data1.get_value(i,'Service_Charges')
                acs = data1.get_value(i,'Actual_Stipend')
                nc = data1.get_value(i,'Name_of_Company')
                wc = data1.get_value(i,'Working_Condition')
                fc = data1.get_value(i,'Facilities')
                others = data1.get_value(i,'others')
                cuv = sc*acs*wc*fc*others

                ac=1
                ivv=0
                tvv=0
                tc=1
                a=0
                tcu=0
                for j in data.index:
                    id2 = data.get_value(j,'Company_ID')
                    month = data.get_value(j,'Month')
                    sv = data.get_value(j,'Services')
                    iv = data.get_value(j,'Invoice Value')
                    unit = data.get_value(j,'Unit')
                    if id1 == id2:
                        ac = unit
                        tcu=a+ac
                        a=tcu
                    if id1 == id2:
                        tc = iv
                        tvv = ivv+tc
                        ivv = tvv
                print(ivv)
                ipp = (tcu/30)*cuv
                ipp = ipp*7
                cur1 = mydb.cursor()
                row=[id1,nc,month,sv,int(tcu),int(ivv),float(ipp)]
                cur1.execute('INSERT INTO ipp_company (Company_ID,Name_of_Company,Months,Services,Unit,Invoice_Value,IPP) VALUES (%s,%s,%s,%s,%s,%s,%s)',row)
                mydb.commit()
                

    return render_template('reports.html')

@app.route('/uploads', methods = ['GET','POST'])
def uploads():
    if request.method == 'POST':
        if request.form['submit_button']=='edit':

            mydb = ms.connect(host='localhost',user='root',password='',database='ipp')

            print('database connected')

            cursor=mydb.cursor()
            csv_data = csv.reader(open('E:/PROJECT/ipp/uploads/sampcomp.csv'))

            for row in csv_data:
                print(row)
                cursor.execute('INSERT INTO company_master_table (Sr_No,Name_of_Company,Company_ID,Month,Unit,Address,State,PinCode,Customer_Contact_Person,Customer_Contact_Number,Supervisor,Reporting_1,Reporting_2,Reporting_3,Reporting_4,Reporting_5,Closed_By,Services_A,Services_Model,Reputation_of_client,Service_Charges,Actual_Stipend,Working_Condition,Facilities,others) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
                print(row)
            mydb.commit()
            cursor.close()


            return redirect(request.url)
        elif request.form['submit_button']=='edit1':

            mydb = ms.connect(host='localhost',user='root',password='',database='ipp')

            print('database connected')

            cursor=mydb.cursor()
            csv_data = csv.reader(open('E:/PROJECT/ipp/uploads/comp.csv'))
            for row in csv_data:
                print(row)
                cursor.execute('INSERT INTO services_invoice (Sr_No,Name_of_Company,Company_ID,Month,Services,Model,Unit,Invoice_Value) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',row)
                print(row)
            mydb.commit()
            cursor.close()


            return redirect(request.url)
        elif request.form['submit_button']=='edit2':

            mydb = ms.connect(host='localhost',user='root',password='',database='ipp')

            print('database connected')

            cursor=mydb.cursor()
            csv_data = csv.reader(open('E:/PROJECT/ipp/uploads/emp1.csv'))
            print(csv_data)
            for row in csv_data:
                print(len(row))
                cursor.execute('INSERT INTO employee_master (Sr_No,Prepared_By,Code,Emp_No,Name,Gender,Father_Name,DOB,DOJ,Paid_By,Cost_Centre,Employee_Name_On_Passbook,Bank_Name,Branch_Name,IFSC_Code,Beneficiary_Account_Number,Beneficiary_City,State,email_address,pay_days,total_days,location,Bank_State,CPI_eligibility,Designation,ODOJ,Level,Direct_Indirect,Reporting_1,Reporting_2,Reporting_3,Reporting_4,Reporting_5,Personal_Official_No,Company) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
                print(row)
            mydb.commit()
            cursor.close()


            return redirect(request.url)

        # check if the post request has the file part
        elif request.form['submit_button']=='Submit':
            if 'file' not in request.files:

                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No file selected for uploading')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash('File successfully uploaded')
                return redirect(request.url)
            else:
                flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
                return redirect(request.url)

        elif request.form['submit_button']=='Submit1':
            if 'file' not in request.files:

                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No file selected for uploading')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash('File successfully uploaded')
                return redirect(request.url)
            else:
                flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
                return redirect(request.url)

        elif request.form['submit_button']=='Submit2':
            if 'file' not in request.files:

                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No file selected for uploading')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash('File successfully uploaded')
                return redirect(request.url)
            else:
                flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
                return redirect(request.url)



@app.route('/comp', methods = ['GET','POST'])
def comp():

    if request.method == "POST":
        Sr_No = request.form['Sr_No']
        Name_of_Company = request.form['Name_of_Company']
        Company_ID = request.form['Company_ID']
        Unit = request.form['Unit']
        Address = request.form['Address']
        State = request.form['State']
        PinCode = request.form['PinCode']
        Customer_Contact_Person = request.form['Customer_Contact_Person']
        Customer_Contact_Number = request.form['Customer_Contact_Number']
        Supervisor = request.form['Supervisor']
        Reporting_1 = request.form['Reporting_1']
        Reporting_2 = request.form['Reporting_2']
        Reporting_3 = request.form['Reporting_3']
        Reporting_4 = request.form['Reporting_4']
        Reporting_5 = request.form['Reporting_5']
        Closed_By = request.form['Closed_By']
        Services_A = request.form['Services_A']
        Services_Model = request.form['Services_Model']
        Reputation_of_client = request.form['Reputation_of_client']
        Service_Charges = request.form['Service_Charges']
        Actual_Stipend = request.form['Actual_Stipend']
        Working_Condition = request.form['Working_Condition']
        Facilities = request.form['Facilities']
        others = request.form['others']
        cur1 = mysql.connection.cursor()
        cur1.execute('INSERT INTO company_master_table (Sr_No,Name_of_Company,Company_ID,Unit,Address,State,PinCode,Customer_Contact_Person,Customer_Contact_Number,Supervisor,Reporting_1,Reporting_2,Reporting_3,Reporting_4,Reporting_5,Closed_By,Services_A,Services_Model,Reputation_of_client,Service_Charges,Actual_Stipend,Working_Condition,Facilities,others) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(Sr_No,Name_of_Company,Company_ID,Unit,Address,State,PinCode,Customer_Contact_Person,Customer_Contact_Number,Supervisor,Reporting_1,Reporting_2,Reporting_3,Reporting_4,Reporting_5,Closed_By,Services_A,Services_Model,Reputation_of_client,Service_Charges,Actual_Stipend,Working_Condition,Facilities,others))
        mysql.connection.commit()
        return redirect(url_for('index'))

    return render_template('comp.html')

@app.route('/dod',methods = ['GET','POST'])
def dod():
    data="";
    data1="";
    b=0;
    c=1;
    if request.method == "POST" :
        if request.form['submit_button']=='Submit':
            Sr_No = request.form['Sr_No']
            Name_of_Company = request.form['Name_of_Company']
            Company_ID = request.form['Company_ID']
            Unit = request.form['Unit']
            Address = request.form['Address']
            State = request.form['State']
            Pincode = request.form['Pincode']
            Customer_Contact_Person = request.form['Customer_Contact_Person']
            Customer_Contact_Number = request.form['Customer_Contact_Number']
            Supervisor = request.form['Supervisor']
            Reporting_1 = request.form['Reporting_1']
            Reporting_2 = request.form['Reporting_2']
            Reporting_3 = request.form['Reporting_3']
            Reporting_4 = request.form['Reporting_4']
            Reporting_5 = request.form['Reporting_5']
            Closed_By = request.form['Closed_By']
            Services_A = request.form['Services_A']
            Services_Model = request.form['Services_Model']
            Reputation_of_client = request.form['Reputation_client']
            Service_Charges = request.form['Service_Charges']
            Actual_Stipend = request.form['Actual_Stipend']
            Working_Condition = request.form['Working_Condition']
            Facilities = request.form['Facilities']
            others = 1

            cur1 = mysql.connection.cursor()
            cursor.execute('INSERT INTO company_master_table (Sr_No,Name_of_Company,Company_ID,Unit,Address,State,PinCode,Customer_Contact_Person,Customer_Contact_Number,Supervisor,Reporting_1,Reporting_2,Reporting_3,Reporting_4,Reporting_5,Closed_By,Services_A,Services_Model,Reputation_of_client,Service_Charges,Actual_Stipend,Working_Condition,Facilities,others) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'(Sr_No,Name_of_Company,Company_ID,Unit,Address,State,PinCode,Customer_Contact_Person,Customer_Contact_Number,Supervisor,Reporting_1,Reporting_2,Reporting_3,Reporting_4,Reporting_5,Closed_By,Services_A,Services_Model,Reputation_of_client,Service_Charges,Actual_Stipend,Working_Condition,Facilities,others))
            mysql.connection.commit()
            return redirect(url_for('index'))
        elif request.form['submit_button']=='search':
            search_rep = request.form['search']

            cur = mysql.connection.cursor()
            cur1 = mysql.connection.cursor()
            cur.execute("SELECT * FROM company_master_table WHERE Company_ID = %s",(search_rep,))
            data = cur.fetchall()
            cur1.execute("SELECT * FROM services_invoice WHERE Company_ID = %s",(search_rep,))
            data1=cur1.fetchall()
            for i in data1:
               b+=i[5]
            cur.close()
    else:
        pass
    return render_template('dod.html',students=data,service=data1,b=b)



@app.route('/update',methods = ['GET','POST'])
def update():
    if request.method == "POST" :
        if request.form['submit_button']=='Submit':
            a = request.form['cars']
            print(a)
    return render_template('update.html')

@app.route('/showReport',methods = ['GET','POST'])
def showReport():
    data3=[]
    if request.method == "POST":
        if request.form['submit_button']=='IPP':
            
            mydb = ms.connect(host='localhost',user='root',password='',database='ipp')
            print('database connected')
            cursor=mydb.cursor()
            cursor.execute("SELECT * FROM ipp_company")
            data3 = cursor.fetchall()
            print(data3)
            data = pd.DataFrame(data3,columns=['Company_ID','Name_of_Company','Month','Services','Unit','Invoice_Value','IPP'])
    return render_template('showReport.html',data1=data3)

@app.route('/cpp',methods = ['GET','POST'])
def cpp():
    data3=[]
    ivv = 0
    cpp=0
    direct1 = 0
    direct2 = 0
    direct3 = 0
    indirect1 = 0
    indirect2 = 0
    indirect3 = 0
    acparts=0
    pid1=0
    pid2=0
    piid1=0
    pid3 = 0
    piid3=0
    piid2=0
    final=0
    td1 = 0
    td2 = 0
    td3 = 0
    tid1 = 0
    tid2 = 0
    tid3 = 0
    if request.method == "POST":
        if request.form['submit_button']=='IPP':
            
            mydb = ms.connect(host='localhost',user='root',password='',database='ipp')
            print('database connected')
            cursor=mydb.cursor()
            cursor.execute("SELECT * FROM ipp_company")
            data3 = cursor.fetchall()
            print(data3)
            data = pd.DataFrame(data3,columns=['Company_ID','Name_of_Company','Months','Services','Unit','Invoice Value','IPP'])
            cursor=mydb.cursor()

            cursor.execute("SELECT * FROM employee_master ")
            data2=cursor.fetchall()
            data1 = pd.DataFrame(data2,columns=['Sr_No','Prepared_By','Code','Emp_No','Name','Gender','Father_Name','DOB','DOJ','Paid_By','Cost_Centre','Employee_Name_On_Passbook','Bank_Name','Branch_Name','IFSC_Code','Beneficiary_Account_Number','Beneficiary_City','State','email_address','pay_days','total_days','location','Bank_State','CPI_eligibility','Designation','ODOJ','Level','Direct_Indirect','Reporting_1','Reporting_2','Reporting_3','Reporting_4','Reporting_5','Personal_Official_No','Company'])
            print(data1['Level'])
            direct1 = 0
            direct2 = 0
            direct3 = 0
            indirect1 = 0
            indirect2 = 0
            indirect3 = 0
            acparts=0
            pid1=0
            pid2=0
            final=0
            piid1=0
            pid3 = 0
            piid3=0
            piid2=0
            td1 = 0
            td2 = 0
            td3 = 0
            tid1 = 0
            tid2 = 0
            tid3 = 0
            for i in data1.index:
                a = data1.get_value(i,'Level')
                b = data1.get_value(i,'Direct_Indirect')
                if a == "1" and b == "Direct":
                    direct1 = direct1 + 1
                elif a == "1" and b == "Indirect":
                    indirect1 = indirect1 + 1
                elif a == "2" and b == "Direct":
                    direct2 = direct2 + 1
                elif a == "2" and b == "Indirect":
                    indirect2 = indirect2 + 1  
            print(direct1)
            ivv = 0
            ivv18 = 0
            cpp = 0
            acparts = 0
            for i in data.index:
                iv = data.get_value(i,'Invoice Value')
                ivv = ivv+iv
            ivv18 = (ivv)/1.18
            print(ivv18)
            cpp = (ivv18*1)/100
            print(cpp)

            d1 = direct1 * 2
            d2 = direct2 * 4
            id1 = indirect1 * 1
            id2 = indirect2 * 2

            final = d1+d2+id1+id2
            print(final)

            acparts = cpp/final
            print(acparts)

            pid1 = acparts * 2
            pid2 = acparts * 4
            pid3 = acparts * 8
            piid1 = acparts * 1
            piid2 = acparts * 2
            piid3 = acparts * 4

            print(pid1)
            print(pid2)
            print(piid1)
            print(piid2)

            td1 = pid1 * direct1
            td2 = pid2 * direct2
            td3 = pid3 * direct3
            tid1 = piid1 * indirect1
            tid2 = piid2 * indirect2
            tid3 = piid3 * indirect3

            print(td1)
            print(td2)
            print(tid1)
            print(tid2)

            print(td1+td2+tid1+tid2)
    return render_template('cpp.html',ivv=ivv,cpp=cpp,final=final,data1=data3,direct1=direct1,direct2=direct2,direct3=direct3,indirect1=indirect1,indirect2=indirect2,indirect3=indirect3,acparts=acparts,piid1=piid1,pid1=pid1,pid2=pid2,pid3=pid3,piid2=piid2,piid3=piid3,td1=td1,td2=td2,td3=td3,tid1=tid1,tid2=tid2,tid3=tid3)
if __name__=='__main__':
    app.run(debug=True)
