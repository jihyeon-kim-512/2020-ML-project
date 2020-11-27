import pymysql
from database import connection, dataProcessing
import numpy as np

from datetime import date, timedelta
from konlpy.tag import Okt

okt = Okt()
txt = okt.morphs('입력준비')
print(txt)

today = date.today()
yesterday = date.today() - timedelta(1)

num = 0

#챗봇 시작 인삿말
def sayHello():
    conn = connection.get_connection()

    sql = "select ans_output from output_ans where ans_id = %s"

    cursor = conn.cursor()
    cursor.execute(sql, ('인사'))
    hello = cursor.fetchall()

    cursor.close()

    return hello


#입력하겠다는 채팅이 들어왔을 때
def sayInput_1(n,userPhone):

    global num
    num = n
    print(num)

    if num == -1:
        print("지출")
    elif num == 1:
        print("수입")

    conn = connection.get_connection()

    sql = '''select ans_output from output_ans where ans_id = %s'''

    cursor = conn.cursor()
    cursor.execute(sql, ('입력'))
    botSay = cursor.fetchall()

    cursor.close()

    return botSay


#채팅 내용 저장
def sayInput_2(json,userPhone):

    global num
    print(num)
    conn = connection.get_connection()

    txt = okt.morphs(json['message'])
    money = 0
    date = ''
    sum=0

    if num !=0 :
        time_list = ['어제', '오늘']

        result = dataProcessing.somethings(json['message'])
        place = result[0]
        print(result[1])
        str = result[1].split(' ')
        for i in str:
            get_ctg = dataProcessing.category(i)

        thing = get_ctg[0]
        ctg = get_ctg[1]

        print(thing)
        print(ctg)


        if time_list[0] in txt:
            date = yesterday.strftime('%Y-%m-%d')
        elif time_list[1] in txt:
            date = today.strftime('%Y-%m-%d')
        else:
            date = today.strftime('%Y-%m-%d')

        for i in range(len(txt)):
            str1=txt[i]

            vv = okt.pos(str1)
            # print(vv)
            if vv[0][1]=='Number' :
                money = vv[0][0]
                sum = dataProcessing.cash_change(money)
            else :
                continue


    if (money != 0) :
        sql = '''insert into assets(date, user_id, place, something, money, inex, category_category_id)
                 values (%s, %s, %s, %s, %s, %s, %s)'''
        cursor = conn.cursor()
        cursor.execute(sql, (date, userPhone, place, thing, sum, num, ctg))
        conn.commit()

    sql = '''insert into chat_said(user_id, said) values (%s, %s)'''
    cursor = conn.cursor()
    cursor.execute(sql, (userPhone, json['message']))
    conn.commit()

    cursor.close()

    return
