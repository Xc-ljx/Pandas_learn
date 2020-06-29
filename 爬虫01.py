#top250的名称、豆瓣评分、评价数、电影概况、电影链接等
#-*- coding = utf-8 -**-

import sys
import re    #正则表达式，文字匹配
from bs4 import BeautifulSoup   #网页解析，获取数据
import urllib.request as urll,urllib.error    #制定URL，获取网络数据
import xlwt        #进行excle操作
import _sqlite3 #进行SQLite操作

def main():
    baseurl = "https://movie.douban.com/top250?start="
    # #1.爬取网页
    # datalist = getData(baseurl)
    # savepath = ".\\豆瓣电影Top250.xls"  #用r就直接/
    # #3.数据保存
    # saveData(savepath)
    askURL("https://movie.douban.com/top250?start=")


#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):       #调用获取页面信息的函数10次
        url = baseurl + str(i*25)
        html = askURL(url)        #保存获取到的网页源码
       # 2.逐一解析数据
    return datalist

#得到指定一个URL的网页内容
def askURL(url):
    head = {    #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like; Gecko) Chrome / 83.0; .4103; .116; Safari / 537.36"
    }
           #用户代理，告诉豆瓣服务器，我们是什么类型的机器、浏览器
    request = urll.Request(url,headers=head)
    html = ""
    try:
        response = urll.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html








#3.数据保存
def saveData(savepath):
    print(" ")




if __name__=="__mian__":   #程序执行时
#调用函数
    main()