from flask import Flask, render_template, session, redirect, flash
from mysqlconnection import MySQLConnector
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

app.run(debug=True)

