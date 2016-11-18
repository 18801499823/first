#!F:\Python27\python.exe
# -*- coding: UTF-8 -*-
print
import urllib
import urllib2
import re
import MySQLdb
print

import urllib
import urllib2
import re

class News:

    #init
    def __init__(self):
        self.url = "http://news.baidu.com/"

    #convert div to ''
    def tranTags(self, x):
        pattern = re.compile('<div.*?</div>')
        res = re.sub(pattern, '', x)
        return res

    #getPage
    def getPage(self):
        url = self.url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    #get titleCode
    def getTitleCode(self):
        page = self.getPage()
        pattern = re.compile('(<div id="pane-news".*?)<div class="column clearfix" id="tupianxinwen">', re.S)
        navCode = re.search(pattern, page)
        return navCode.group(1)

    #get nav
    def getTitle(self):
        navCode = self.getTitleCode()
        pattern = re.compile('<a href="(.*?)".*?>(.*?)</a>', re.S)
        itmes = re.findall(pattern, navCode)
        return itmes
        #for item in itmes:
        #    print item[0], self.tranTags(item[1])




#news = News()
#news.getTitle()

# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","grab",charset="GBK")
# 使用cursor()方法获取操作游标
cursor = db.cursor()

news = News()
new=news.getTitle()

for item in new:
    print item[0],news.tranTags(item[1])
    title = news.tranTags(item[1])
    # SQL 插入语句
    sql = "INSERT INTO title(title,url)VALUES('"+title+"','"+item[0]+"')"
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

