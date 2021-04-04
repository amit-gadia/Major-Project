from flask import *
import mysql.connector
import datetime
import os
conn=mysql.connector.connect(host="localhost",user="root",password="Root",database="cms",auth_plugin="mysql_native_password")
cur=conn.cursor(buffered=True)
app = Flask(__name__)
app.secret_key="CMSPU"
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\safezone\\Desktop\\finalprj\\templates\\notice\\files'
DOWNLOAD_DIRECTORY = 'C:\\Users\\safezone\\Desktop\\finalprj\\templates\\notice\\cfiles'
@app.route('/downloadnotice/<file>')
def down(file):
    print(file)
    return send_from_directory(DOWNLOAD_DIRECTORY, file, as_attachment=True)
class adminnotice:
    @app.route("/tnotice")
    def notice():
        st="maintemp/admin_main.html"
        return render_template(st,temp="/noticeicon")
    @app.route("/noticeicon")
    def show_noticemain():
        st="maintemp/"+session['userrole']+"main.html"
        return render_template("notice/addnotice.html")
    @app.route("/addnewnote",methods=['POST'])
    def add_notice():
        date=request.form['date']
        title=request.form['title']
        description=request.form['description']
        eventtype=request.form['eventtype']
        file=request.files['event_file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
        event_file=file.filename
        print(event_file)
        timing=str(datetime.datetime.now())
        sql="insert into notice(date,name,details,category,file,timestamp)values(%s,%s,%s,%s,%s,%s);"
        val=(date,title,description,eventtype,event_file,timing)
        cur.execute(sql,val)
        conn.commit()
        return view_notice.show_notice()

class Student:
    @app.route("/add_student")  
    def addStudent():
        st="maintemp/admin_main.html"
        return render_template(st,temp="/stu")

    @app.route("/stu")
    def add_stu():
        return render_template('adduser/addstu_form.html')
class Placement:
    @app.route("/add_placement")  
    def addPlacement():
        st="maintemp/admin_main.html"
        return render_template(st,temp="/pla")

    @app.route("/pla")
    def add_pla():
        return render_template('adduser/addpla_form.html')

class Faculty:
    @app.route("/add_faculty")  
    def addFaculty():
        st="maintemp/admin_main.html"
        return render_template(st,temp="/fac")

    @app.route("/fac")
    def add_fac():
        return render_template('adduser/addfac_form.html')
class Warden:
    @app.route("/add_warden")  
    def addWarden():
        st="maintemp/admin_main.html"
        return render_template(st,temp="/war")
        
    @app.route("/war")
    def add_war():
        return render_template('adduser/addwar_form.html')

class Accounts:
    @app.route("/add_accounts")  
    def addAccounts():
        st="maintemp/admin_main.html"
        return render_template(st,temp="/acc")
        
    @app.route("/acc")
    def add_acc():
        return render_template('adduser/addacc_form.html')
class Transport:
    @app.route("/add_transport")  
    def addTransport():
        st="maintemp/admin_main.html"
        return render_template(st,temp="/tra")
        
    @app.route("/tra")
    def add_tra():
        return render_template('adduser/addtra_form.html')
class Library:
    @app.route("/add_library")  
    def addLibrary():
        st="maintemp/admin_main.html"
        return render_template(st,temp="/lib")
        
    @app.route("/lib")
    def add_lib():
        return render_template('adduser/addlib_form.html')

class add_roles:
    @app.route("/addnewrole",methods=['POST'])
    def add_role():
        f_n=request.form['f_n']
        l_n=request.form['l_n']
        date=request.form['date']
        Qualification=request.form['Qualification']
        salary=request.form['salary']
        customRadio=request.form['customRadio']
        aano=request.form['aano']
        bg=request.form['bg']
        role=request.form['role']
        sql="select id from users;"
        cur.execute(sql)
        id=cur.fetchall()
        sql="insert into role(fname,lname,dob,qualification,salary,gender,aano,bg,role)values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val=(f_n,l_n,date,Qualification,salary,customRadio,aano,bg,role)
        cur.execute(sql,val)xx
        userid=role+"@"+f_n+l_n+str(id[-1][0]+1)
        password=role+"@123"
        name=f_n+l_n
        sql="insert into users(name,user_id,passwd,role)values(%s,%s,%s,%s);"
        val=(name,userid,password,role)
        cur.execute(sql,val)
        conn.commit()
        if(role=="Warden"):
            return Warden.add_war()
        elif(role=="Placement"):
            return Placement.add_pla()
        elif(role=="Accounts"):
            return Accounts.add_acc()
        elif(role=="Transport"):
            return Transport.add_tra()
        elif(role=="Library"):
            return Library.add_lib()

class view_notice:
    @app.route("/notice")
    def view_notice():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/shownotice")
    @app.route("/shownotice")
    def show_notice():
        sql="select id,date,name,details,category,file from notice order by id desc;"
        cur.execute(sql)
        data=cur.fetchall()
        print(data)
        st="maintemp/"+session['userrole']+"main.html"
        return render_template("notice/viewnotice.html",t=len(data),c=data)
class main():
    @app.route("/")
    def index():
        return render_template('welcomescreen.html')
    @app.route("/login")
    def login():
        return render_template('login.html',error="All Fields are Manodatry")
    @app.route('/addlogin',methods=['POST'])
    def hello_world():
        if(request.method=='POST'):
            a=request.form['userid']
            b=request.form['passcode']
            sql="select role,name,user_id from users where user_id=%s and passwd=%s;"
            val=a,b
            cur.execute(sql,val)
            gg=cur.fetchall()
            print(len(gg))
            if(len(gg)==1):
                print(gg)
                session['userid']=gg[0][2]
                session['user']=gg[0][1]
                session['userrole']=gg[0][0]
                print(session)
                st="maintemp/"+gg[0][0]+"_main.html"
                print(st)
                return render_template(st)
                    
            else:
                erro="The User Id and Password is Incorrect"
                return render_template('login.html',error=erro)
            
        return "Hello"

app.run(debug=True,host="0.0.0.0")