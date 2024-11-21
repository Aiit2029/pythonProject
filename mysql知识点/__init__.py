import pymysql

conn=pymysql.connect(host='127.0.0.1', port='3306',user='root', password='root',db='day53', charset='utf8')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = 'select * from day53'

cursor.execute(sql)
print(cursor.fetchall())

cursor.close()
conn.close()
