from datetime import date, timedelta
from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO
import pymysql
from database import moneyDAO, botDAO, joinDAO, modifyDAO, deleteDAO, excelExport
import time
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CHAT_SECRET#'
socketio = SocketIO(app)

userPhone=''

@app.route('/')
def start():
    print(userPhone)
    return render_template('membership_form.html')

@app.route('/', methods=['GET', 'POST'])
def start2():
    id = request.form['ID']
    pw = request.form['PW']

    if not (id and pw) :
        return render_template('membership_form.html')

    else:
        chk = joinDAO.login(id, pw)
        if chk == id:
            global userPhone
            userPhone = chk
            print("user" + userPhone)
            return redirect('/chatmain/')
        else:
            return render_template('membership_form.html')




@app.route('/chatstart/')
def chat_start():
    return render_template('chat_start.html')


@app.route('/chatstart/', methods=['GET', 'POST'])
def chatstart():
    print('pass')
    userName = request.form['name']
    userSsn = request.form['ssn']
    userselect = request.form['select']
    userPhone = request.form['phone']
    pw = request.form['pw']

     # 회원가입시 주민등록번호와 전화번호 자리 수가 맞지 않을 때

    if not (userName and userSsn and userPhone and pw) :

        return render_template('chat_start.html')

     # 회원가입시 주민등록번호와 전화번호 자리 수가 맞지 않을 때
    elif len(userSsn) != 6:

        return render_template('chat_start.html')

    elif len(userPhone) != 11:

        return render_template('chat_start.html')

    print(userName, userPhone, userSsn, userselect)
    a = joinDAO.joinUser(userName, userSsn, userPhone, userselect, pw)



    if a == False:
        return render_template('chat_start.html')
    else:
        return redirect('/')




@app.route('/imgpre/')
def img_pre():
    return render_template('img_pre.html')

@app.route('/chatmain/', methods=['GET', 'POST'])
def chat_start2():
    global userPhone
    print('main '+ userPhone)
    # userName = request.form['name']
    # userPhone = request.form['phone']
    # print(userName, userPhone)

    moneySum = moneyDAO.moneySum(userPhone)
    eMoney = moneyDAO.moneyExpend(userPhone)
    iMoney = moneyDAO.moneyIncome(userPhone)

    return render_template('chat_main.html', moneySum=moneySum[0][0], eMoney=eMoney[0][0], iMoney=iMoney[0][0])


@app.route('/chatsetting/')
def chat_setting():
    global userPhone
    limit = joinDAO.limitChk(userPhone)
    return render_template('chat_setting.jsp', limit=limit[0][0])


@app.route('/limitmoney/', methods=['GET', 'POST'])
def limit_money():
    global userPhone
    limit = request.form['limit']
    joinDAO.limitMoney(userPhone, limit)
    return redirect('/chatsetting/')


@app.route('/excelExport/')
def excel_export():
    global userPhone
    print('excel'+userPhone)
    excelExport.excelExport(userPhone)
    return redirect('/chatsetting/')


@app.route('/summoney/', methods=['GET', 'POST'])
def sum_money():
    AM = moneyDAO.AllDetail(userPhone)
    print(AM)
    return render_template('sum_money.jsp', AM=AM)

@app.route('/inmoney/')
def in_money():
    IM = moneyDAO.InDetail(userPhone)

    return render_template('in_money.jsp', IM=IM)


@app.route('/exmoney/')
def ex_money():
    EM = moneyDAO.ExDetail(userPhone)

    return render_template('ex_money.jsp', EM=EM)

@app.route("/inputform/")
def input_form():
    return render_template('input_form.html')

@app.route("/dbinput/",methods=['GET', 'POST'] )
def input_form2():
    print('pass')
    global userPhone

    what_money = request.form['whatmoney']
    m_category = request.form['mcategory']
    date = request.form['date']
    content = request.form['content']
    money = request.form['money']

    print(m_category,what_money)
    moneyDAO.formInput(userPhone, what_money, m_category, date, content, money)

    return redirect('/summoney/')



@app.route("/updateform/<p1>/<p2>/<p3>/<p4>/<p5>/<p6>", methods=['GET', 'POST'])
def update_form(p1, p2, p3, p4, p5, p6):
    return render_template('update_form.jsp', p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6)


@app.route("/dbupdate/<path>",methods=['GET', 'POST'] )
def update_form2(path):
    print(path)

    what_money = request.form['whatmoney']
    m_category = request.form['mcategory']
    date = request.form['date']
    content = request.form['content']
    money = request.form['money']

    print(m_category,what_money)
    moneyDAO.formUpdate(userPhone, what_money, m_category, date, content, money, path)

    return redirect('/summoney/')


@app.route('/chatbot/')
def chat_bot():
    return render_template('chat_bot.html')



@app.route('/chatimage/')
def chat_image():
    return render_template('img_pre.html')



def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')



@socketio.on('connect')
def start_event():
    hello = botDAO.sayHello()

    for i in range(0,3):
        socketio.emit('start_chat', hello[i])


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    socketio.emit('my response', json, callback=messageReceived)

    global userPhone

    if ("지출" in json.setdefault('message') and "입력" in json.setdefault('message')) :
        userIn = botDAO.sayInput_1(-1,userPhone)
        socketio.emit('start_chat', userIn)

    if ("수입" in json.setdefault('message') and "입력" in json.setdefault('message')) :
        userIn = botDAO.sayInput_1(1,userPhone)
        socketio.emit('start_chat', userIn)

    if ("여기까지" in json.setdefault('message')) :
        botDAO.sayInput_1(0,userPhone)
        socketio.emit('start_chat', '네, 처리해 드렸습니다 :>')

    botDAO.sayInput_2(json,userPhone)


@app.route('/chatmember/', methods = ['GET', 'POST'])
def chat_member():
    global userPhone
    userInfo = joinDAO.userinfo(userPhone)
    return render_template('chat_member_modify.html', userInfo=userInfo)



@app.route('/update/', methods = ['GET', 'POST'])
def updateDB():
    global userPhone
    userName = request.form.get('name')
    pw = request.form.get('pw')

    print(userName)

    if not (userName and pw) :
        return render_template('chat_member_modify.html')

    modifyDAO.modifyUser(userName, pw, userPhone)

    return redirect('/chatmember/')





@app.route('/delete/', methods = ['GET', 'POST'])
def deleteDB():
    global userPhone
    userName = request.form.get('name')
    pw = request.form.get('pw')

    print('delete')

    if not (userName and pw) :
        return render_template('chat_member_modify.html')

    deleteDAO.deleteUser(userName, pw, userPhone)

    return redirect('/')




if __name__ == '__main__':
    socketio.run(app, debug=True)
