from flask import Flask,request,render_template,session,redirect
from sqlhelper import py_mysql,py_mysql_all,py_mysql_one
from flask_settings import time1
app = Flask(__name__)

app.secret_key='dsfda'
@app.before_request
def v():
    if request.path == "/login":
        return None
    if session.get("user"):
        return None
    else:
        return redirect("/login")

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    sql = "SELECT username FROM userinfo WHERE username=%s AND password=%s"
    user = py_mysql(sql,(username,password))
    if user:
        session['user'] = username
        return redirect('/index')
    else:
        return render_template("login.html", msg="用户名密码错")

@app.route('/index',methods=["POST", "GET"])
def index():
    if request.method == 'GET':
        metting_list = time1
        sql = 'select name,id from meetingroom'
        room_list = py_mysql_all(sql)
        return render_template('index.html',metting_list=metting_list,room_list=room_list)
    metting_list = time1
    sql = 'select name,id from meetingroom'
    room_list = py_mysql_all(sql)

    date = request.form.get('date')
    # sql = 'select user,room,timeline from reserverecord where data=%s ORDER BY timeline'
    sql ='select userinfo.username,meetingroom.name,reserverecord.timeline from reserverecord left join userinfo on reserverecord.user=userinfo.id left join meetingroom on meetingroom.id=reserverecord.room WHERE data=%s ORDER BY reserverecord.timeline'
    list = py_mysql_all(sql,date)
    user_list = []
    dic = {}
    for i in list:
        user = i[2]
        dic[user] = {}
    for i in list:
        user = i[2]
        room = i[1]
        dic[user][room] = 1
        user_list.append(user)

    return render_template('index.html',metting_list=metting_list,room_list=room_list,user_list=user_list,date=date,dic=dic)

@app.route('/post_list',methods=['POST'])
def post_list():
    date = request.form.get('date')
    id = request.form.get('id')
    time,room = id.split(':')
    username = session.get('user')
    sql = 'select id from userinfo WHERE username=%s'
    b = py_mysql_one(sql, username)
    user_id = b[0]
    sql = 'select id from reserverecord WHERE DATA=%s and timeline=%s and user=%s and room=%s'
    a1 = py_mysql(sql, (date, time, user_id, room))
    if a1:
        sql = 'DELETE FROM reserverecord WHERE DATA=%s and timeline=%s and user=%s and room=%s'
        py_mysql(sql, (date, time, user_id, room))
        return 'b'
    sql = 'INSERT into reserverecord(data,timeline,user,room) VALUE (%s,%s,%s,%s)'
    py_mysql(sql,(date,time,user_id,room))
    return 'a'
if __name__ == '__main__':
    app.run(debug=True)


