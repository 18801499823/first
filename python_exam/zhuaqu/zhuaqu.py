#!F:\Python27\python.exe
# -*- coding: UTF-8 -*-

print "Content-type:text/html"
print                               # 空行，告诉服务器结束头部

import urllib,re,urllib2
#获取页面
url = "http://news.baidu.com/?qq-pf-to=pcqq.group"

content=urllib.urlopen(url).read()
#正则匹配
#searchObj = re.search('<div id="channel-all" class="channel-all clearfix" >.*?<ul class="clearfix">.*?<li class="icon-new-wrapper">.*?<li>.*?<a href=.*?>.*?<div id="body" alog-alias="b">', content, re.I|re.S|re.U)

searchObj = re.search('<div id=\"channel-all\" class=\"channel-all clearfix\" >.*?<div id=\"body\" alog-alias=\"b\">', content, re.I|re.S|re.U)

if searchObj:
   print "searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"