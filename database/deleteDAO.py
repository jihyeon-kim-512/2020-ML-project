import pymysql
from database import connection
import numpy as np

def deleteUser(userName, pw, userPhone):

    conn = connection.get_connection()
    print('a')
    try:
        sql = "select * from user_table where phone_num = %s and pw = %s"
        cursor = conn.cursor()
        cursor.execute(sql, (userPhone, pw))
        data = cursor.fetchall()

        match = False

        if  data:
            match = True
            print("삭제했습니다.")
            sql = "delete from user_table where phone_num = %s"
            cursor.execute(sql, userPhone)
            data = cursor.fetchall()


        else:
           print("삭제할 수 없습니다.")
           match = False

        print(data)

        conn.commit()



    finally:
        cursor.close()

    return match
