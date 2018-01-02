#安装python -m pip install pymysql
import pymysql
#链接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='P@ssword',db='test')
#创建cursor
cur = conn.cursor()

#创建执行SQL语句
#cur.execute("insert into scptest1(sid,sname) values (%s, %s)", ['3', 'Michael'])
cur.execute("insert into scptest1(sid,sname) values (5, 'haha')")

#返回受影响行数
print(cur.rowcount)
cur.execute("SELECT * FROM scptest1")

#返回查询结果
print (cur.fetchall())

#插入数据后要提交事物
conn.commit()

#关闭cursor
cur.close()

#关闭数据库链接
conn.close()
