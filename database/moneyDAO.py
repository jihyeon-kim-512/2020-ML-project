import pymysql
from database import connection
from datetime import datetime

now = datetime.now()
mm=now.month

#금액 합계 함수
def moneySum(userPhone):
    conn = connection.get_connection()

    sql = '''
        select sum(case when inex=1 then money end)
        	   - sum(case when inex=-1 then money end)
        from assets
        where month(date) = %s and user_id = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (mm, userPhone))
    MS = cursor.fetchall()

    cursor.close()
    print(MS)
    return MS


#지출 금액 함수
def moneyExpend(userPhone):
    conn = connection.get_connection()

    sql = '''
        select sum(money)
        from assets
        where (inex=-1 and month(date) = %s) and user_id = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (mm, userPhone))
    IM = cursor.fetchall()

    cursor.close()

    return IM


#수입 금액 함수
def moneyIncome(userPhone):
    conn = connection.get_connection()

    sql = '''
        select sum(money)
        from assets
        where (inex=1 and month(date) = %s) and user_id = %s
    '''


    cursor = conn.cursor()
    cursor.execute(sql, (mm, userPhone))
    EM = cursor.fetchall()

    cursor.close()

    return EM


#금액 합계 함수
def AllDetail(userPhone):
    conn = connection.get_connection()

    sql = '''
        select date, money, place, something, inex, category_category_id, assets_id from assets
        where month(date) = %s and user_id = %s
        order by date desc;
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (mm,userPhone))
    AD = cursor.fetchall()
    cursor.close()

    return AD

#금액 수입 함수
def InDetail(userPhone):
    conn = connection.get_connection()

    sql = '''
        select date, money, place, something, inex, category_category_id, assets_id from assets
        where (inex=1 and month(date) = %s) and user_id = %s
        order by date desc;
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (mm, userPhone))
    ID = cursor.fetchall()
    cursor.close()

    return ID

#금액 지출 함수
def ExDetail(userPhone):
    conn = connection.get_connection()

    sql = '''
        select date, money, place, something, inex, category_category_id, assets_id from assets
        where (inex=-1 and month(date) = %s) and user_id = %s
        order by date desc;
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (mm, userPhone))
    ED = cursor.fetchall()
    cursor.close()

    return ED


# 직접입력 폼
def formInput(userPhone, what_money, m_category, date, content, money):
    conn = connection.get_connection()

    if what_money == 'a':
        what_money = -1
    elif what_money == 'b':
        what_money = 1

    if m_category == '의류':
        m_category = 1
    elif m_category == '뷰티':
        m_category = 2
    elif m_category == '생활비':
        m_category = 3
    elif m_category == '여행':
        m_category = 4
    elif m_category == '교통비':
        m_category = 5
    elif m_category == '식비':
        m_category = 6
    elif m_category == '월급':
        m_category = 7
    elif m_category == '용돈':
        m_category = 8
    elif m_category == '기타':
        m_category = 9

    print(m_category)
    sql = '''
            insert into assets(date, user_id, place, something, money, inex, category_category_id)
            values (%s, %s, %s, %s, %s, %s, %s);
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (date, userPhone, '', content, money, what_money, m_category))
    conn.commit()
    cursor.close()

    return


# 수정 폼
def formUpdate(userPhone, what_money, m_category, date, content, money, path):
    conn = connection.get_connection()

    if what_money == 'a':
        what_money = -1
    elif what_money == 'b':
        what_money = 1

    if m_category == '의류':
        m_category = 1
    elif m_category == '뷰티':
        m_category = 2
    elif m_category == '생활비':
        m_category = 3
    elif m_category == '여행':
        m_category = 4
    elif m_category == '교통비':
        m_category = 5
    elif m_category == '식비':
        m_category = 6
    elif m_category == '월급':
        m_category = 7
    elif m_category == '용돈':
        m_category = 8
    elif m_category == '기타':
        m_category = 9

    print(m_category)
    sql = '''
            UPDATE assets SET date=%s, place=%s, something=%s, money=%s, inex=%s, category_category_id =%s
            where assets_id = %s;
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (date, '', content, money, what_money, m_category, path))
    conn.commit()
    cursor.close()

    return
