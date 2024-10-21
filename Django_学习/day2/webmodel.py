import pymysql


def register(username,password):

    conn = pymysql.connect(host='127.0.0.1', port=3306,user='root', password='root', db='day53', charset='utf8')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    select_sql = 'select * from userinfo where username="%s" and password="%s"'
    cur.execute(select_sql,(username,password))
    flag = cur.fetchone()
    if flag:
        exit('当前用户已存在')
    else:
        insert_sql = 'insert into userinfo(username,password) values(%s,%s)'
        cur.execute(insert_sql, (username, password))
        cur.commit()

    cur.close()
    conn.close()


def login(username,password):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='day53', charset='utf8')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    select_sql = 'select * from userinfo where username="%s" and password="%s"'
    cur.execute(select_sql,(username,password))
    flag = cur.fetchone()
    if flag:
        return True
    else:

        return False



