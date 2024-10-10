import pymysql


conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root',passwd = 'root',database = 'pycharmproject')
cur = conn.cursor()
while True:
    try:
        sql =input('>>>').strip()
        if sql == 'exit':
            break
        else:
            cur.execute(sql)
            conn.commit()
            ret = cur.fetchall()
            # ret = cur.fetchone()
            # ret = cur.fetchmany(10)
            print(ret)
    except Exception as e:
        print(e)
        conn.rollback()
    # except pymysql.err.ProgrammingError as e:
    #     print(e)
cur.close()
conn.close()

    #     print('没有这个数据库')