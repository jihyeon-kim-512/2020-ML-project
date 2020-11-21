import pymysql
from database import connection
import numpy as np
from datetime import datetime

now = datetime.now()
mm=now.month

#금액 합계 함수
def moneySum():
    conn = connection.get_connection()

    sql = '''
        select sum(case when inex=1 then money end)
        	   - sum(case when inex=-1 then money end)
        from assets
        where month(date) = %s;
    '''

    cursor = conn.cursor()
    cursor.execute(sql, mm)
    MS = cursor.fetchall()

    cursor.close()
    print(MS)
    return MS


#지출 금액 함수
def moneyExpend():
    conn = connection.get_connection()

    sql = '''
        select sum(money)
        from assets
        where inex=-1 and month(date) = %s;
    '''

    cursor = conn.cursor()
    cursor.execute(sql, mm)
    IM = cursor.fetchall()

    cursor.close()

    return IM


#수입 금액 함수
def moneyIncome():
    conn = connection.get_connection()

    sql = '''
        select sum(money)
        from assets
        where inex=1 and month(date) = %s;
    '''


    cursor = conn.cursor()
    cursor.execute(sql, mm)
    EM = cursor.fetchall()

    cursor.close()

    return EM


#금액 합계 함수
def AllDetail():
    conn = connection.get_connection()

    sql = '''
        select date, money, place, something, inex from assets
        where month(date) = %s
        order by date desc;
    '''

    cursor = conn.cursor()
    cursor.execute(sql, mm)
    AD = cursor.fetchall()
    cursor.close()

    return AD

#금액 수입 함수
def InDetail():
    conn = connection.get_connection()

    sql = '''
        select date, money, place, something from assets
        where inex=1 and month(date) = %s
        order by date desc;
    '''

    cursor = conn.cursor()
    cursor.execute(sql, mm)
    ID = cursor.fetchall()
    cursor.close()

    return ID

#금액 지출 함수
def ExDetail():
    conn = connection.get_connection()

    sql = '''
        select date, money, place, something from assets
        where inex=-1 and month(date) = %s
        order by date desc;
    '''

    cursor = conn.cursor()
    cursor.execute(sql, mm)
    ED = cursor.fetchall()
    cursor.close()

    return ED
