import pymysql
from database import connection
import numpy as np

#금액 합계 함수
def moneySum():
    conn = connection.get_connection()

    sql = '''
        select sum(case when inex=1 then money end)
        	   - sum(case when inex=0 then money end)
        from assets;
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
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
        where inex=0
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    IM = cursor.fetchall()

    cursor.close()

    return IM


#수입 금액 함수
def moneyIncome():
    conn = connection.get_connection()

    sql = '''
        select sum(money)
        from assets
        where inex=1;
    '''


    cursor = conn.cursor()
    cursor.execute(sql)
    EM = cursor.fetchall()

    cursor.close()

    return EM


#금액 합계 함수
def AllDetail():
    conn = connection.get_connection()

    sql = '''
        select date, money, place, inex from assets
        order by date desc;
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    AD = cursor.fetchall()
    cursor.close()
    
    return AD

#금액 수입 함수
def InDetail():
    conn = connection.get_connection()

    sql = '''
        select date, money, place from assets
        where inex=1
        order by date desc;
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    ID = cursor.fetchall()
    cursor.close()

    return ID

#금액 지출 함수
def ExDetail():
    conn = connection.get_connection()

    sql = '''
        select date, money, place from assets
        where inex=0
        order by date desc;
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    ED = cursor.fetchall()
    cursor.close()

    return ED
