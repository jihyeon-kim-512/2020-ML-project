import pymysql
from database import connection
import numpy as np

def modifyUser(name, pw, userPhone):

    conn = connection.get_connection()

    try:
        sql = "select * from user_table where phone_num = %s"
        cursor = conn.cursor()
        cursor.execute(sql, userPhone)
        data = cursor.fetchall()



        match = False

        if  data:
            match = True
            print("수정했습니다.")
            sql = "update user_table SET name = %s where phone_num = %s"
            cursor.execute(sql, (name, userPhone))
            data = cursor.fetchall()


        else:
           print("수정할 수 없습니다.")
           match = False

        print(data)

        conn.commit()



    finally:
        cursor.close()

    return match
