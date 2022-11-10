from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        Conn = sqlite3.connect("./static/users.db")
        cur = Conn.cursor()    
        cur.execute("select * from users where Name = ?",(user,))
        userCreds = cur.fetchone()
        cur.close() 
        Conn.close()
        if userCreds==None or userCreds[1]!=pwd:
            return 'Login Failed'
        return render_template('profile.html')

@app.route('/register',methods = ['POST','GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        Conn = sqlite3.connect("./static/users.db")
        cur = Conn.cursor()    
        cur.execute("INSERT into users VALUES (?,?);",(user,pwd))
        Conn.commit()
        cur.close() 
        Conn.close()
        return render_template('login.html')

if __name__ == '__main__':
   app.run()
