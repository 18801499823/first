#!F:\Python27\python.exe
# -*- coding: UTF-8 -*-

print "Content-type:text/html"
print                               # 空行，告诉服务器结束头部

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","sql" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM datas"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()

   #for row in results:
           #print row
   for row in results:
       for roe in row:
           print roe
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()