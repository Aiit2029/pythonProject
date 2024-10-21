import pymysql

name = input('>>>姓名:').strip()
age = input('>>>年龄:').strip()

conn = pymysql.connect(host='127.0.0.1', port=3306,user='root', password='root', db='day53', charset='utf8')

cur = conn.cursor(pymysql.cursors.DictCursor)
sql = 'insert into mydb1 (name, age) values (%s, %s)'

cur.execute(sql,(name,age))
conn.commit()

cur.close()
conn.close()
