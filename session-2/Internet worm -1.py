# 需要调用的requests 库和 BeautifulSoup库中的bs4工具

from flask import Flask,request,render_template
import requests
from bs4 import BeautifulSoup
import urllib.request
import re
from flask_cors import CORS






# 定义一个变量url，为需要爬取数据我网页网址
url1 = 'https://snowstar.org'
url2 = 'https://snowstar.org/page/2/'
# 获取这个网页的源代码，存放在req中，{}中为不同浏览器的不同User-Agent属性，针对不同浏览器可以自行百度
req1 = requests.get(url1, {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'})
req2 = requests.get(url2, {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'})

# 生成一个Beautifulsoup对象，用以后边的查找工作
soup = BeautifulSoup(req1.text, 'lxml')
soup2 = BeautifulSoup(req2.text, 'lxml')
# 找到所有p标签中的内容并存放在xml这样一个类似于数组队列的对象中
xml = soup.find_all('a', herf_='')
xml2 = soup2.find_all('span', class_='posted-date')
#利用循环将xml[]中存放的每一条打印出来
for i in range(len(xml2)):
    name = xml2[i].string
    for i in range(len(xml)):
        msg = xml[i].string
        print(msg,name)

# import requests
# import re
# content = requests.get('https://snowstar.org').text
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
# results = re.findall(pattern, content)
# print(results)
#
# for result in results:
#     url,name,author,date = result
#     author = re.sub('\s','',author)
#     date = re.sub('\s','',date)
#     print(url,name,author,date)











