from flask import Flask,request,render_template
import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="",database="pylogin")
cursor = conn.cursor()


app = Flask(__name__)

@app.route("/login_validation",methods=['POST'])
def login_validation():
    email = request.form.get("email")
    password = request.form.get("password")
    cursor.execute("""SELECT * FROM `login` WHERE `email` LIKE '{}' AND `pass` LIKE '{}' """.format(email,password))
    user = cursor.fetchall()
    if len(user)>0:
        return "<h1>home page</h1>"
    else:
        return "<h1>something went wrong check username and password</h1>"
    # print(user)
    # return "hello"

@app.route("/signup_validation",methods=['POST'])
def signup_validation():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")
    address = request.form.get("address")
    cursor.execute("""insert into login values('{}','{}','{}','{}','{}')""".format(fname,lname,email,password,address))
    conn.commit()
    return "<h1>sign up successfull. go to <a href='/'>login </a> page</h1>"


@app.route("/")
def login():
    
    return  render_template("login.html")

@app.route("/forgot")
def forgot():
    return  render_template("forgot.html")

@app.route("/signup")
def signup():
    return  render_template("signup.html")

if __name__=='__main__':
    app.run(debug=True)