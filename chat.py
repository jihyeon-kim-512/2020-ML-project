from datetime import date, timedelta
from flask import Flask, render_template, request
from flask_socketio import SocketIO
import pymysql
from database import moneyDAO, botDAO, joinDAO
import time
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CHAT_SECRET#'
socketio = SocketIO(app)


@app.route('/')
def chat_start():
    return render_template('chat_start.html')

@app.route('/imgpre/')
def img_pre():
    return render_template('img_pre.html')

@app.route('/chatmain/', methods=['POST'])
def chat_start2():
    print('pass')
    userName = request.form['name']
    userPhone = request.form['phone']
    print(userName, userPhone)

    moneySum = moneyDAO.moneySum()
    eMoney = moneyDAO.moneyExpend()
    iMoney = moneyDAO.moneyIncome()

    return render_template('chat_main.html', moneySum=moneySum[0][0], eMoney=eMoney[0][0], iMoney=iMoney[0][0])


@app.route('/summoney/')
def sum_money():
    AM = moneyDAO.AllDetail()

    return render_template('sum_money.jsp', AM=AM)

@app.route('/inmoney/')
def in_money():
    IM = moneyDAO.InDetail()

    return render_template('in_money.jsp', IM=IM)


@app.route('/exmoney/')
def ex_money():
    EM = moneyDAO.ExDetail()

    return render_template('ex_money.jsp', EM=EM)



@app.route('/chatbot/')
def chat_bot():
    return render_template('chat_bot.html')



@app.route('/chatimage/')
def chat_image():
    return render_template('chat_image.html')



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

    if ("입력" in json.setdefault('message')) :
        InOut = True
        userIn = botDAO.sayInput_1()
        socketio.emit('start_chat', userIn)

    if ("여기까지" in json.setdefault('message')) :
        socketio.emit('start_chat', '네, 처리해 드렸습니다 :>')

    botDAO.sayInput_2(json)



if __name__ == '__main__':
    socketio.run(app, debug=True)
