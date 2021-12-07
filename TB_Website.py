from flask import Flask,request,redirect,url_for
from flask import render_template
import Module.doaction as doaction
import Module.TB as TB
import time

App = Flask(__name__)
DB = doaction.DBInI()
TBSys = TB
 
def GetTime() :
    t = time.localtime()
    return time.strftime("%Y/%m/%d,%H:%M:%S",t)

def CheckAccount(name,psw) : 
    Data = DB.OtherCmd("SELECT UserName,PSW FROM Account WHERE USERNAME = " + f"'{name}'")
    if Data != None :
        print(Data)
        return True
    else : 
        return False
    

@App.route('/')
def home():
    return render_template('mainpage.html')

@App.route("/AfterLogin", methods=["POST","GET"])
def afterlogin() :
    if request.method == "POST":
        user_name = request.form["nm"]
        psw = request.form["psw"]
        data = TBSys.GetDeviceInfo("https://demo.thingsboard.io","Email Address","PSW")
        #print(data)
        return data
    else :
        return "Login Wrong!!"

@App.route("/regist", methods=["POST","GET"])
def register():
    return render_template("register.html")

@App.route("/RegistSucess", methods=["POST","GET"])
def afteregist() :
    if request.method == "POST":
        user_name = request.form["nm"]
        psw = request.form["psw"]
        
        if not CheckAccount(user_name,psw) :
           DB.AddData("Account","UserName,PSW,TimeStamp",f"'{user_name}','{psw}','{GetTime()}'")

        return redirect(url_for("userr",usr = (user_name)))
    else :
        return "Regist Wrong!!"

def run() :
    App.run()

@App.route('/<usr>')
def userr(usr):
    return f"<h1>{usr} - Success</h1>"

@App.route('/<usr>')
def login(usr,data):
    return f"<h1>{usr} - Success</h1> <br> {data}"

if __name__ == "__main__":
   run()