from flask import Flask, render_template, session, redirect, flash, request
from mysqlconnection import MySQLConnector
import md5
app = Flask(__name__)
mysql = MySQLConnector(app,'dashboard')
app.secret_key = "fdefdfede..e.fd.fd.fd.f.df.da..e3e.3.3.43.r.tr4.4.!!!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/users')
def users():
    query = "SELECT * FROM users;"
    users = mysql.query_db(query)
    return render_template('users.html', users=users)
@app.route('/login-page')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    valid = True
    if request.form['email'] == "":
        valid = False
        flash("Email cannot be empty", 'danger')
    if request.form['password'] == "":
        valid = False
        flash("Password cannot be empty", 'danger')
    if not valid:
        return redirect("/")
    else:
        query = "SELECT * FROM users WHERE email = :email AND password = :password"
        data = {
            "email":request.form['email'],
            "password": md5.new(request.form['password']).hexdigest()
        }
        user = mysql.query_db(query, data)
        if len(user) != 0:
            session['id'] = user[0]['id']
            session['first_name'] = user[0]['first_name']
            session['last_name'] = user[0]['last_name']
            return redirect('/')
    return redirect('/login-page')

app.run(debug=True)

