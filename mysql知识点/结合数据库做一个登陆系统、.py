import pymysql

#
username = input("username:").strip()
password = input("password:").strip()

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',database='pycharmproject')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select * from user_info where username= %s and password= %s'
cur.execute(sql,(username,password))

user_db = cur.fetchall()
if user_db:
    print(user_db)
    print('登陆成功')

    cur.execute('update user_info set status=1 where username="%s" and password="%s"'%(username,password))
    conn.commit()

else:
    print('报错')
# print(user_db)
# for i in user_db:
#     if username == i['username'] and password == i['password']:
#         print('登陆成功')
#
#     else:
#         print('登陆失败')


