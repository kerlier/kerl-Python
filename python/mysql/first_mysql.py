#!/usr/bin/python3
import MySQLdb

username = "root"
password = "root"
dbUrl = "192.168.5.134"
db_charSet = "utf8"
db_name = "test"

# 连接数据库
connect = MySQLdb.connect(dbUrl, username, password, db_name, charset=db_charSet)

# 获取游标
cursor = connect.cursor()

selectSql = "select * from user"
# 使用execute执行sql语句
cursor.execute(selectSql)

# 使用fetchAll来获取所有的数据
print(cursor.fetchall())

# 最后关闭游标
cursor.close()

# 最后关闭连接
connect.close()