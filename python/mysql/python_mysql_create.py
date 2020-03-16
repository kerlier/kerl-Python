#!/usr/bin/python3

import MySQLdb

import logging

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)
username = "root"
password = "root"
dbUrl = "192.168.5.134"
db_charSet = "utf8"
db_name = "test"


createTableSql = """
    create table EMPLOYEE(
       FIRST_NAME char(20) not null,
       LAST_NAME  char(20),
       AGE int,
       SEX char(1),
       INCOME float
    )
"""

connect = MySQLdb.connect(dbUrl, username, password, db_name, charset=db_charSet)

cursor = connect.cursor()

try:
    logging.info("execute create sql...")

    cursor.execute(createTableSql)

    logging.info("end to execute create sql")

    logging.info("commit")
    connect.commit()
except:
    logging.error("occur error, rollback")
    connect.rollback()

finally:
    logging.info("close cursor")
    logging.info("close connect")
    cursor.close()
    connect.close()
