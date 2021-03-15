from flask import *
import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="finalprj",auth_plugin="mysql_native_password")
cur=conn.cursor(buffered=True)
sql='show tables;'

cur.execute(sql)
print(cur.fetchall())
