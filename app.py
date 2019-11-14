from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import os
from flask_wtf import Form
import urllib.request
from flask_wtf.file import FileField
import csv
import mysql.connector as ms
from werkzeug.utils import secure_filename

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

@app.route('/uploads', methods = ['GET','POST'])
def uploads():
    if request.method == 'POST':
        if request.form['submit_button']=='edit':

            mydb = ms.connect(host='localhost',user='root',password='',database='ipp')

            print('database connected')

            cursor=mydb.cursor()
            csv_data = csv.reader(open('E:/PROJECT/ipp/uploads/sample1.csv'))
            for row in csv_data:
                cursor.execute('INSERT INTO company_master_table (Sr_No,Name_of_Company,Company_ID,Unit,Address,State,PinCode,Customer_Contact_Person,Customer_Contact_Number,Supervisor,Reporting_1,Reporting_2,Reporting_3,Reporting_4,Reporting_5,Closed_By,Services_A,Services_Model,Reputation_of_client,Service_Charges,Actual_Stipend,Working_Condition,Facilities) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
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

        cur1 = mysql.connection.cursor()
        cur1.execute('INSERT INTO company_master_table (Sr_No,Name_of_Company,Company_ID,Unit,Address,State,PinCode,Customer_Contact_Person,Customer_Contact_Number,Supervisor,Reporting_1,Reporting_2,Reporting_3,Reporting_4,Reporting_5,Closed_By,Services_A,Services_Model,Reputation_of_client,Service_Charges,Actual_Stipend,Working_Condition,Facilities) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(Sr_No,Name_of_Company,Company_ID,Unit,Address,State,PinCode,Customer_Contact_Person,Customer_Contact_Number,Supervisor,Reporting_1,Reporting_2,Reporting_3,Reporting_4,Reporting_5,Closed_By,Services_A,Services_Model,Reputation_of_client,Service_Charges,Actual_Stipend,Working_Condition,Facilities))
        mysql.connection.commit()
        return redirect(url_for('index'))

    return render_template('comp.html')

@app.route('/dod',methods = ['GET','POST'])
def dod():
    data="";
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

            cur1 = mysql.connection.cursor()
            cursor.execute('INSERT INTO company_master_table (Sr_No,Name_of_Company,Company_ID,Unit,Address,State,PinCode,Customer_Contact_Person,Customer_Contact_Number,Supervisor,Reporting_1,Reporting_2,Reporting_3,Reporting_4,Reporting_5,Closed_By,Services_A,Services_Model,Reputation_of_client,Service_Charges,Actual_Stipend,Working_Condition,Facilities) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'(Sr_No,Name_of_Company,Company_ID,Unit,Address,State,PinCode,Customer_Contact_Person,Customer_Contact_Number,Supervisor,Reporting_1,Reporting_2,Reporting_3,Reporting_4,Reporting_5,Closed_By,Services_A,Services_Model,Reputation_of_client,Service_Charges,Actual_Stipend,Working_Condition,Facilities))
            mysql.connection.commit()
            return redirect(url_for('index'))
        elif request.form['submit_button']=='search':
            search_rep = request.form['search']

            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM company_master_table WHERE Unit = %s",(search_rep,))

            data = cur.fetchall()
            print(data);
            cur.close()
    else:
        pass
    return render_template('dod.html',students=data)




if __name__=='__main__':
    app.run(debug=True)
