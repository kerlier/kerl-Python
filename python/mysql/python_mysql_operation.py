#!/usr/bin/python3

import MySQLdb
import logging
from employee import Employee

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)


username = "root"
password = "root"
dbUrl = "192.168.5.134"
db_charSet = "utf8"
db_name = "test"


def getConnection():
    connect = MySQLdb.connect(dbUrl, username, password, db_name, charset=db_charSet)
    return connect


def selectRows(selectSql):
    employees = []
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute(selectSql)
    rows = cursor.fetchall()

    try:
        for row in rows:
            employee = Employee(row[0], row[1], row[2], row[4], row[3])
            employees.append(employee)
    except:
        logging.error("query error")
    finally:
        logging.info("close connection")
        cursor.close()
        connection.close()
    return employees


def insertEmployee(employees):
    connection = getConnection()
    cursor = connection.cursor()
    insertSql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (%s, %s, %s, %s, %s)"

    try:
        logging.info("insert data...")
        cursor.executemany(insertSql, employees)
        connection.commit()
    except MySQLdb.DatabaseError as e:
        logging.error("insert data error",e)
        connection.rollback()
    finally:
        logging.info("close connection")
        cursor.close()
        connection.close()


if __name__ == '__main__':

    # selectSql = "select * from EMPLOYEE"
    # employees = selectRows(selectSql)
    # logging.info("employee' size is %d" % len(employees))
    # for employee  in employees:
    #     print(employee.firstName, employee.lastName, employee.age, employee.inCome, employee.sex)
    employee = Employee("firstName", "lastName", 10, 800.0, "M")
    employees = []
    employees.append(employee)
    insertEmployee(employees)
