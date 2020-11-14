import pymysql

def get_connection():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='machinegun',
        db='mydb',
        charset='utf8'
    )

    return conn
