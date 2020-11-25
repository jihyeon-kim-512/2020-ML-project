import pymysql
import pandas as pd
from database import connection

def excelExport(userPhone) :
    conn = connection.get_connection()

    sql = '''
        select date, place, something, money, inex, category_category_id
        from assets
        where user_id = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, userPhone)
    result = cursor.fetchall()

    # excel 저장
    date, place, something, money, inex, category_category_id = [],[],[],[],[],[]

    for i in range(0, len(result)):
        date.append(result[i][0])
        place.append(result[i][1])
        something.append(result[i][2])
        money.append(result[i][3])
        inex.append(result[i][4])
        category_category_id.append(result[i][5])


    raw_data = {
                '날짜' : date,
                '장소' : place,
                '내역' : something,
                '금액' : money,
                '지출(-1)/수입(1)' : inex,
                '항목' : category_category_id }


    raw_data1 = pd.DataFrame(raw_data)
    xlxs_dir='20201124.xlsx'

    with pd.ExcelWriter(xlxs_dir) as writer:
        raw_data1.to_excel(writer, sheet_name='Sheet1', index=False)
