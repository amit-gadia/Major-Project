from flask import *
import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="Root",database="cms",auth_plugin="mysql_native_password")
cur=conn.cursor(buffered=True)
sql='show tables;'

cur.execute(sql)
print(cur.fetchall())
