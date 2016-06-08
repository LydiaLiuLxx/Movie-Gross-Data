#-*- encoding:utf-8 -*-
'''
import urllib
import urllib2
import re
import sys
import os
import requests


def getHtmlContent(url):
    global defaultWaitTime
    content=None
    retry = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
    AccessFrequency = defaultWaitTime
    while retry < 5:
        try:
            r = requests.get(url,timeout=10,headers=headers)
            content = r.content
            return content
        except:
            retry+=1
            time.sleep(AccessFrequency)
    return content

reload(sys)
sys.setdefaultencoding('utf-8')

defaultWaitTime = 1
dr = 'wdzj'

page = 1
url = 'http://movie.douban.com/subject/26726098/comments?start=40&limit=20&sort=new_score'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    
    
    content=urllib2.urlopen(url).read()
    print content
    pattern=re.compile('class=.*?pname">(.*?)</a>.*?<td class=.*?col_a40001"><span><b>(.*?)</b>.*?<td>(.*?)<input .*?>.*?<span title="(.*?)">.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td><label id="syl_.*?">(.*?)</label></td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
    items = re.findall(pattern,content)
    count=0
    
       
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

'''
import urllib2
import re
import time
def movie(movieTag):

    tagUrl=urllib2.urlopen(url)
    tagUrl_read = tagUrl.read().decode('utf-8')
    return tagUrl_read
def subject(tagUrl_read):
    ''' 
        这里还存在问题：
        ①这只针对单独的一页进行排序，而没有对全部页面的电影进行排序
        ②下次更新添加电影链接，考虑添加电影海报
        ③需要追加列表
        ④导入到本地txt或excel中
        ⑤在匹配电影名字时是否可以同时匹配链接与名字、评分、评论组成数组
        ⑥
    '''
#正则表达式匹配电影的名字（链接）、评分与评论    
    nameURL = re.findall(r'(http://movie.douban.com/subject/[0-9.]+)\/"\s+title="(.+)"',tagUrl_read)
    scoreURL = re.findall(r'<span\s+class="rating_nums">([0-9.]+)<\/span>',tagUrl_read)
    evaluateURL = re.findall(r'<span\s+class="pl">\((\w+)人评价\)<\/span>',tagUrl_read)
    movieLists = list(zip(nameURL,scoreURL,evaluateURL))
    newlist.extend(movieLists)
    return newlist
#用quote处理特殊（中文）字符
# movie_type = urllib.request.quote(input('请输入电影类型(如剧情、喜剧、悬疑)：'))
page_end=100#int(input('请输入搜索结束时的页码：'))
num_end=page_end*20
num=0
page_num=1
newlist=[]
while num<num_end:
    url=r'http://movie.douban.com/tag/剧情?start=0'#%(movie_type,num)
    movie_url = movie(url)
    subject_url=subject(movie_url)
    num=page_num*20
    page_num+=1
else:
    #使用sorted函数对列表进行排列，reverse参数为True时升序，默认或False时为降序， key=lambda还不是很明白这里的原理
    movieLIST = sorted(newlist, key=lambda movieList : movieList[1],reverse = True)
    for movie in movieLIST:
        print(movie)

time.sleep(3)

