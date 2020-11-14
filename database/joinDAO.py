import pymysql
from database import connection
import numpy as np


def joinUser():
    conn = connection.get_connection()

    sql = '''insert into chat_test(test_word) values (%s)'''

    cursor = conn.cursor()
    cursor.execute(sql, (str(json)))
    conn.commit()

    cursor.close()

    return
