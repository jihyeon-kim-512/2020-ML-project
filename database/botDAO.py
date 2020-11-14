import pymysql
from database import connection
import numpy as np
import re

from datetime import date, timedelta
from konlpy.tag import Okt

okt = Okt()
txt = okt.morphs('입력준비')
print(txt)

today = date.today()
yesterday = date.today() - timedelta(1)

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
def sayInput_1():
    conn = connection.get_connection()

    sql = '''select ans_output from output_ans where ans_id = %s'''

    cursor = conn.cursor()
    cursor.execute(sql, ('입력'))
    botSay = cursor.fetchall()

    cursor.close()

    return botSay


#채팅 내용 저장
def sayInput_2(json):
    print('send')

    conn = connection.get_connection()

    txt = okt.morphs(json['message'])
    money = 0
    date = ''
    sum=0

    time_list = ['어제', '오늘']

    if time_list[0] in txt:
        date = yesterday.strftime('%Y-%m-%d')
    elif time_list[1] in txt:
        date = today.strftime('%Y-%m-%d')
    else:
        date = today.strftime('%Y-%m-%d')

    for i in range(len(txt)):
        str1=txt[i]

        vv = okt.pos(str1)
        print(vv)
        if vv[0][1]=='Number' :
            money = vv[0][0]
            for a in re.finditer('원', money) :
                endstr = a.start()
                try :
                    sum += int(money[:endstr])
                except :
                    money = (money[:endstr])
                    print('e')
                print(sum)
            for b in re.finditer('십', money) :
                bs = b.start()
                be = b.end()
                sum += int(money[:bs] + '0' + money[be:])
                print(sum)
            for b in re.finditer('백', money) :
                bs = b.start()
                be = b.end()
                sum += int(money[:bs] + '00' + money[be:])
                print(sum)
            for b in re.finditer('천', money) :
                bs = b.start()
                be = b.end()
                sum += int(money[:bs] + '000' + money[be:])
                print(sum)
            for b in re.finditer('만', money) :
                bs = b.start()
                be = b.end()
                sum = int(money[:bs] + '0000' + money[be:])
                print(sum)

        else :
            continue

        print('날짜: ' + date + '\n금액: ' + str(sum))

    if (money != 0) :
        sql = '''insert into chat_content(date, user_id, money) values (%s, %s, %s)'''
        cursor = conn.cursor()
        cursor.execute(sql, (date, json['user_name'], sum))
        conn.commit()

    sql = '''insert into chat_said(user_id, said) values (%s, %s)'''
    cursor = conn.cursor()
    cursor.execute(sql, (json['user_name'], json['message']))
    conn.commit()

    cursor.close()

    return
