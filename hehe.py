
from flask import Flask, render_template, request
from database import moneyDAO
from datetime import datetime

now = datetime.now()
mm=now.month

app = Flask(__name__)

@app.route('/')
def formpage():
    return render_template('FormPage.html')

@app.route('/view',methods=['POST'])
def view():
    userName = request.form['userName']
    userPw = request.form['userPw']
    userEmail = request.form['userEmail']
    print(userName)


@app.route('/line')
def line():
    print('linepass')
    in_mon = moneyDAO.linechart('01000000001', 1)
    ex_mon = moneyDAO.linechart('01000000001', -1)
    print(in_mon[0][0], ex_mon[1][0])
    incnt = len(in_mon)
    excnt = len(ex_mon)
    return render_template('googlechart.html', in_mon=in_mon, ex_mon=ex_mon, incnt=incnt, excnt=excnt, mm=mm)


@app.route('/pie')
def pie():
    print('piepass')
    result = moneyDAO.categoryMoney('01000000001', -1)

    for i in range(0,len(result)):
        if result[i] == None:
            result[i] = 0

    print(result)
    return render_template('piechart.html', result=result)



if __name__ == "__main__":
    app.run(debug=True)
