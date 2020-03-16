#!/usr/bin/python3

import MySQLdb
import logging
username = "root"
password = "root"
dbUrl = "192.168.5.134"
db_charSet = "utf8"
db_name = "test"

# 连接数据库
connect = MySQLdb.connect(dbUrl, username, password, db_name, charset=db_charSet)

# 字符串必须是 '""'
newWord = '"lvshuzhen"'
tableName = "user"

# 实现update_sql
updateSql = "update %s set passWord= %s where userName = %s" % (tableName, newWord, '"yang"')

cursor = connect.cursor()

try:

    # 执行语句
    logging.info("execute %s " % updateSql)
    cursor.execute(updateSql)

    logging.info("提交操作")
    # 提交操操作
    connect.commit()
except MySQLdb.DatabaseError as e:
    print(e)
    logging.error("提交失败，回滚事务")
    connect.rollback()
finally:
    logging.info("关闭连接")
    cursor.close()
    connect.close()

