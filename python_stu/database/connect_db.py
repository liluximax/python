#!/usr/bin/python3
import mysql.connector
from datetime import datetime
try:
	conn = mysql.connector.connect(host='115.29.51.206', user='root', password='llx', database='my')
	cursor = conn.cursor();
	sql = 'select * from emp'
	cursor.execute(sql)
	result = cursor.fetchall()
	cursor.close()
except Exception as e:
	print(e)

print(result)

try:
	now = datetime.now()
	cursor = conn.cursor()
	cursor.execute('insert into emp (ename, hiredate, sal) values (%s, %s, %s)', ['python', str(now), str(1000)])
	# 提交事务
	conn.commit()
	cursor.close()
except Exception as e:
	print(e)
