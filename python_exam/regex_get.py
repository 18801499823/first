#!F:\Python27\python.exe
# -*- coding: UTF-8 -*-

print "Content-type:text/html"
print                               # 空行，告诉服务器结束头部

# CGI处理模块
import cgi, cgitb
import re
import MySQLdb
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
names = form.getvalue('names')
pwd  = form.getvalue('pwd')
email  = form.getvalue('email')
phone  = form.getvalue('phone')

# 检测用户名

match = re.match(r'^[a-z]\w{5,17}', names)

if match:
    print match.group()
else:
    print '<font style="color:red">用户名由6-18位的字母数字下划线组成，不能由数字开头</font><br />'

#检测密码
match = re.match(r'^\w{6,}', pwd)
if match:
    print match.group()
else:
    print '<font style="color:red">密码长度不少于6位</font><br />'

#检测手机号
match = re.match(r'^1[3,5,8]\d{9}', phone)
if match:
    print match.group()
else:
    print '<font style="color:red">手机号必须是13/15/18开头，并为11位</font><br />'

#检测邮箱
match = re.match(r'^\w+@\w+(\.)(com|net|cn|edu)', email)
if match:
    print match.group()
else:
    print '<font style="color:red">邮箱必须包含@符号，后缀为com、net、cn、edu</font><br />'


# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","sql" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO users(names,pwd, email,phone)VALUES('"+names+"','"+pwd+"','"+email+"','"+phone+"')"
#print sql
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
