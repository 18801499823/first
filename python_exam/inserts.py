#!F:\Python27\python.exe
# -*- coding: UTF-8 -*-

print "Content-type:text/html"
print                               # 空行，告诉服务器结束头部

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","sql" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO datas(names,
         content, age)
         VALUES ('h1', 'rt', 20)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()