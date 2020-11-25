import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import pymysql
import pandas as pd
from datetime import datetime

now = datetime.now()
mm=now.month

print(mm)

from database import connection


conn = connection.get_connection()

sql = '''
    select date, place, something, money, inex, category_category_id
    from assets
    where user_id =%s
'''

cursor = conn.cursor()
cursor.execute(sql, '01032323232')
result = cursor.fetchall()

# CSV 저장
# f = open("assets_export.csv", "w")
#
# singers = ["날짜", "장소", "내역", "금액", "지출(-1)/수입(1)", "항목"]
# for i in range(len(singers)):
#     f.write(singers[i] + ',')
#
# for i in range(0, len(result)):
#     f.write('\n')
#     for j in range(0, len(result[i])):
#         print(result[i][j], end=' ')
#         f.write(str(result[i][j]) + ',')
#     print('\n')
#
#
# f.close()
#
#
# cursor.close()



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
xlxs_dir='assets_export.xlsx'

with pd.ExcelWriter(xlxs_dir) as writer:
    raw_data1.to_excel(writer, sheet_name='Sheet1', index=False)
