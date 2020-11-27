import pymysql
from database import connection
import numpy as np


def joinUser(name, ssn, phone_num, phone_company, pw):
    conn = connection.get_connection()

    try:
        sql = "select * from user_table where phone_num = %s"
        cursor = conn.cursor()
        cursor.execute(sql, phone_num)
        data = cursor.fetchall()

    # 휴대전화번호가 DB에 있는 경우
        check = False

        if data:
            print("이미 있는 번호입니다.")
            check = False

        else:
            check = True
            print("가입되었습니다.")
            sql = '''insert into user_table(name, ssn, phone_num, phone_company, pw) values (%s, %s, %s, %s, %s)'''
            cursor.execute(sql, (name, ssn, phone_num, phone_company, pw))
            data = cursor.fetchall()
            print(data)

            conn.commit()

    finally:
        cursor.close()

    return check


def login(id, pw):
    conn = connection.get_connection()


    sql = "select phone_num from user_table where phone_num = %s and pw = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (id, pw))
    data = cursor.fetchall()

# 휴대전화번호가 DB에 있는 경우
    check = ''

    if data :
        if data[0][0] == id:
            check = data[0][0]

    else:
        check = False


    cursor.close()

    return check


def userinfo(userPhone):
    conn = connection.get_connection()

    sql = "select * from user_table where phone_num = %s"
    cursor = conn.cursor()
    cursor.execute(sql, userPhone)
    userInfo = cursor.fetchall()


    cursor.close()

    return userInfo


def limitMoney(userPhone, money):
    conn = connection.get_connection()

    sql = "update user_table SET limit_m = %s where phone_num = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (money, userPhone))
    conn.commit()

    cursor.close()

    return

def limitChk(userPhone):
    conn = connection.get_connection()

    sql = "select limit_m from user_table where phone_num = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (userPhone))
    limit = cursor.fetchall()


    cursor.close()

    return limit

def limitChange(userPhone):
    conn = connection.get_connection()

    sql = "update user_table set limit_m = null where phone_num = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (userPhone))
    conn.commit()

    cursor.close()

    return
