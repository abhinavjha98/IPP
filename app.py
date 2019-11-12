from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf import Form
from flask_wtf.file import FileField
from werkzeug import secure_filename
app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ipp'

mysql = MySQL(app)

@app.route('/')
def index():

    return render_template('index2.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    class excel_file(Form):
        csv_label = FileField("Your CSV")
    return render_template('upload.html')
@app.route('/comp', methods = ['GET','POST'])
def comp():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        comp_name = request.form['comp_name']
        comp_uid = request.form['comp_uid']
        comp_address = request.form['comp_address']
        comp_location = request.form['comp_location']
        comp_GSTN = request.form['comp_GSTN']
        comp_description = request.form['comp_description']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO company_table (comp_name,comp_uid,comp_address,comp_location,comp_GSTN,comp_description) VALUES (%s, %s, %s,%s,%s,%s)", (comp_name, comp_uid,comp_address,comp_location,comp_GSTN,comp_description))
        mysql.connection.commit()
        return redirect(url_for('index'))

    return render_template('comp.html')

@app.route('/dod',methods = ['GET','POST'])
def dod():
    data="";
    if request.method == "POST" :

        if request.form['submit_button']=='Submit':
            reputation_client = request.form['reputation_client']
            print(reputation_client);
            training_fee = request.form['training_fee']
            stipend = request.form['stipend']
            working_condition = request.form['working_condition']
            transport_canteen_facility = request.form['transport_canteen_facility']
            others = request.form['others']
            defaults = request.form['defaults']

            cur1 = mysql.connection.cursor()
            cur1.execute("INSERT INTO dod_table (reputation_client,training_fee,stipend,working_condition,transport_canteen_facility,others) VALUES (%s, %s, %s, %s,%s,%s)", (reputation_client,training_fee,stipend,working_condition,transport_canteen_facility,others))
            mysql.connection.commit()
            return redirect(url_for('index'))
        elif request.form['submit_button']=='search':
            search_rep = request.form['search']
            cur = mysql.connection.cursor()
            cur.execute("SELECT  * FROM dod_table WHERE reputation_client = %s",(search_rep))

            data = cur.fetchall()
            print(data);
            cur.close()
    else:
        pass
    return render_template('dod.html',students=data)

if __name__=='__main__':
    app.run(debug=True)
