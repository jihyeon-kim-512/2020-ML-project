# import nlptest
#
# json = {
#     'name'  : "KJH",
#     'msg'   : "어제 1000원짜리 김밥을 먹었다"
# }
#
# print(json)
# nlptest.haha(json)
# print('*' + str(json))

from flask import Flask, render_template, request

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


if __name__ == "__main__":
    app.run()
