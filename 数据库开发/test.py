import pymysql
# 建立连接
conn = pymysql.connect(
	host='127.0.0.1',
	port=3306,
	user='root',
	password='123456',
	db='db5',
	charset='utf8'
)
user = input('user >>>')
pwd = input('pwd >>>')
# 拿到游标
cursor = conn.cursor()

# 执行sql语句
sql = 'select * from userinfo where user=%s and password=%s'
rows = cursor.execute(sql,(user,pwd))#解决mysql注入问题

# 关闭连接
cursor.close()
conn.close()
if rows:
	print('111')
else:
	print(rows)