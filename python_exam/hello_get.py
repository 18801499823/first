#!F:\Python27\python.exe
# -*- coding: UTF-8 -*-

# CGI处理模块
import cgi, cgitb,MySQLdb

print "Content-type:text/html"
print                               # 空行，告诉服务器结束头部

# 打开数据库连接
db = MySQLdb.connect("127.0.0.1","root","root","sql" )
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('names')
site_content  = form.getvalue('content')
site_age  = form.getvalue('age')


# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO `datas` (names,content,age) values ("+"'"+site_name+"'"+","+"'"+site_content+"'"+","+"'"+site_age+"'"+")"
#print sql
try:
   # 执行sql语句
    cursor.execute(sql)
   # 提交到数据库执行
    db.commit()
#except:
    Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()