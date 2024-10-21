import pymysql

# name = input('>>>姓名:').strip()
# age = input('>>>年龄:').strip()


def select_func():
    conn = pymysql.connect(host='127.0.0.1', port=3306,user='root', password='root', db='day53', charset='utf8')

    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from mydb1'

    cur.execute(sql)
    rows = cur.fetchone()

    cur.close()
    conn.close()
    return rows


