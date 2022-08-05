from flask import Flask, jsonify, render_template, redirect, url_for
import argparse
import cv2

import urllib.request

from flask import request
from flask import abort
from flask import make_response
#from flask_mysqldb import MySQL
import mysql.connector as mysql




def connection():
    
    connection = mysql.connect(
            user='root',
            password='password',
            database='database',
            host='127.0.0.1'
            )
    
    cursor = connection.cursor()
    return cursor, connection
    


application = app = Flask(__name__, template_folder='templates')

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/',  methods =["GET", "POST"])
def index():

      # return redirect(url_for('success', name = Team_name))


    return render_template('index.html')

@app.route('/sign_page', methods=["GET", "POST"])
def sign_in():
    
    if request.method == "POST":
        
        username = request.form["nameuser"]
        username = str(username)
        
        name = request.form["name"]
        name = str(name)
       
       
        email = request.form["mail"]
        email = str(email)
      
       
        password = request.form["pass"]
        password = str(password)
       
       

       
       
        insert_stmt = ("INSERT INTO user(name,username,  email, password)" "VALUES (%s, %s, %s, %s)")
        data = (name, username, email, password)
       
        connect, conn = connection()
       #connect.execute("INSERT INTO database.task (ID, Team_name, lead_name, firstname, secondname, thirdname, fourthname) VALUES (?,?,?,?,?,?,?)")
        connect.execute(insert_stmt, data)
        conn.commit()
        connect.close()
        conn.close()
       
    return render_template('signup.html')


@app.route('/log_in', methods=["GET", "POST"])
def log_in():
    
    if request.method == "POST":
        
    
        user = request.form.get("my_user")
        user = str(user)
        print(user)
    
        password = request.form.get("password")
        password = str(password)
        
        print(password)
        
    
        connect, conn = connection()
       #connect.execute("INSERT INTO database.task (ID, Team_name, lead_name, firstname, secondname, thirdname, fourthname) VALUES (?,?,?,?,?,?,?)")
        result = connect.execute('SELECT * FROM user WHERE username = %s AND password = %s', (user, password))
        print(result)
        
        
        
        account = connect.fetchone()
        
        if account:
            return redirect('/user_page')
        else:
            return redirect('/log_in')
            
        conn.commit()
        connect.close()
        conn.close()
       
    return render_template('login.html')


@app.route('/user_page', methods=["GET", "POST"])
def user_page():
    return render_template('user.html')

@app.route('/task')
def task():
    
    
    if request.method == "POST":
        
    
        task_id = request.form.get("task_ID")
        task_id = int(task_id)
      
    
        password = request.form.get("task_name")
        password = str(password)
        
        detail = request.form.get("text")
        detail = str(detail)
        
        
        insert_stmt = ("INSERT INTO user(id,Task_name,  task)" "VALUES (%s, %s, %s)")
        data = (task_id, password, detail)
       
        connect, conn = connection()
       #connect.execute("INSERT INTO database.task (ID, Team_name, lead_name, firstname, secondname, thirdname, fourthname) VALUES (?,?,?,?,?,?,?)")
        connect.execute(insert_stmt, data)
        conn.commit()
        connect.close()
        conn.close()
    return render_template('task.html')  


@app.route('/team')
def team():
    return render_template('teamdet.html')     
    
    


if __name__ == '__main__':
    app.run(debug=False)