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




@app.route('/task', methods=["GET", "POST"])
def task():
    
    if request.method == "POST":
        
        
        task_id = request.form["task_id"]
        task_id = str(task_id)
        print(task_id)
      
    
        password = request.form["task_name"]
        password = str(password)
        print(password)
        
        detail = request.form["task_detail"]
        detail = str(detail)
        print(detail)
        
        
        insert_stmt = ("INSERT INTO tasks(id,task_name, task)" "VALUES (%s, %s, %s)")
        data = (task_id, password, detail)
       
        new_con, conny = connection()
    
    
    
       #connect.execute("INSERT INTO database.task (ID, Team_name, lead_name, firstname, secondname, thirdname, fourthname) VALUES (?,?,?,?,?,?,?)")
        new_con.execute(insert_stmt, data)
        conny.commit()
        new_con.close()
        conny.close()
    
    return render_template('new_task.html')
        #return render_template('task.html')


@app.route('/team', methods=["GET", "POST"])
def team():
    if request.method == "POST":
        
        #team_id = request.form["team_id"]
        #team_id = str(team_id)
        #print(team_id)
      
    
        team_name = request.form["team_name"]
        team_name = str(team_name)
        print(team_name)
        
        team_lead = request.form["team_leader"]
        team_lead = str(team_lead)
        print(team_lead)
        
        team_1 = request.form["team_1"]
        team_1 = str(team_1)
        
        
        team_2 = request.form["team_2"]
        team_2 = str(team_2)
        
        team_3 = request.form["team_3"]
        team_3 = str(team_3)
        
        team_4 = request.form["team_4"]
        team_4 = str(team_4)
        
        
        insert_stmt = ("INSERT INTO team(Team_name,Leader_name, Name_1, Name_2, Name_3, Name_4)" "VALUES (%s, %s, %s, %s, %s, %s)")
        data = (team_name, team_lead, team_1, team_2, team_3, team_4)
       
        new_con, conny = connection()
    
    
    
       #connect.execute("INSERT INTO database.task (ID, Team_name, lead_name, firstname, secondname, thirdname, fourthname) VALUES (?,?,?,?,?,?,?)")
        new_con.execute(insert_stmt, data)
        conny.commit()
        new_con.close()
        conny.close()
        
    return render_template('teamdet.html')     


@app.route('/append_task', methods=["GET", "POST"])
def append_task():
    if request.method == "GET":
        
        #team_id = request.form["team_id"]
        #team_id = str(team_id)
        #print(team_id)
      
    
        team_name = request.form["team_name"]
        team_name = str(team_name)
        print(team_name)
        
        team_lead = request.form["team_leader"]
        team_lead = str(team_lead)
        print(team_lead)
        
        team_1 = request.form["team_1"]
        team_1 = str(team_1)
        
        
        team_2 = request.form["team_2"]
        team_2 = str(team_2)
        
        team_3 = request.form["team_3"]
        team_3 = str(team_3)
        
        team_4 = request.form["team_4"]
        team_4 = str(team_4)
        
        
        insert_stmt = ("INSERT INTO team(Team_name,Leader_name, Name_1, Name_2, Name_3, Name_4)" "VALUES (%s, %s, %s, %s, %s, %s)")
        data = (team_name, team_lead, team_1, team_2, team_3, team_4)
       
        new_con, conny = connection()
    
    
    
       #connect.execute("INSERT INTO database.task (ID, Team_name, lead_name, firstname, secondname, thirdname, fourthname) VALUES (?,?,?,?,?,?,?)")
        new_con.execute(insert_stmt, data)
        conny.commit()
        new_con.close()
        conny.close()
        
    return render_template('teamdet.html')     

    


if __name__ == '__main__':
    app.run(debug=False)