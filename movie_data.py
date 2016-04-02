#-*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys
import os
import requests
import time
from openpyxl import Workbook
from re import sub


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
month="1"
reload(sys)
sys.setdefaultencoding('utf-8')
wb = Workbook()
sheet = wb.active
title=['Day','Date','Rank','Gross','Theaters','Theaters_Avg','Gross_to_date','Day_num']
defaultWaitTime = 1
try:
    
    content = getHtmlContent("http://www.boxofficemojo.com/monthly/?view=releasedate&chart=&month="+month+"&yr=2016&sort=open&order=DESC")
    print content
    pattern=re.compile('<font size="2"><a href="/movies/\?id=(.*?)">(.*?)</a></font>.*?"',re.S)

    items = re.findall(pattern,content)
    count=0
    # print items
    url="http://www.boxofficemojo.com/movies/?page=daily&view=chart&id="
    for item in items:
        try:
            sheet.title=item[1]
        except:
            if len(item[0])>=30:
                sheet.title=item[0][0:30]
            else:
                sheet.title=item[0][0:-4]
        print item
        movie_content=getHtmlContent(url+item[0])
        date='<td align="center"><font size="2"><a href="/daily.*?<b>(.*?)</b>.*?'
        rank='<td align="center"><font size="2">(.*?)</font></td>.*?'
        gross='<td align="right"><font size="2">\$(.*?)</font></td>.*?'
        rate='<td align="right"><font size="2">.*?</font></td>.*?<td align="right"><font size="2">.*?</font></td>.*?'
        theaters='<td align="right"><font size="2">(.*?)</font></td>.*?'
        avg='<td align="right"><font size="2">\$(.*?)</font></td>.*?'
        gross_to_date='<td align="right"><font size="2">\$(.*?)</font></td>.*?'
        day='<td align="center"><font size="2">(.*?)</font></td>.*?'
        movie_pattern=re.compile('<tr bgcolor="#f.*?f"><td align="center"><font size="2">(.*?)</font></td>.*?'+date+rank+gross+rate+theaters+avg+gross_to_date+day+'</tr>.*?',re.S)
        movies_table=re.findall(movie_pattern,movie_content)
        print movies_table
        
        
        for record in movies_table:
            list1=list(record)
            list1[3]=int(sub(r'[^\d.]', '', list1[3]))
            list1[4]=int(sub(r'[^\d.]', '', list1[4]))
            list1[5]=int(sub(r'[^\d.]', '', list1[5]))
            list1[6]=int(sub(r'[^\d.]', '', list1[6]))
            sheet.append(list1)
        if len(movies_table)!=0:
            sheet=wb.create_sheet()
            sheet.append(title)
    wb.remove_sheet(sheet)
    wb.save("movie_gross_"+month+".xlsx")

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
