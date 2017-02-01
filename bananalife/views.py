#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
import urllib
import re
import urllib2
from bs4 import BeautifulSoup


def index(request):
    if 'search' in request.GET:
        result = request.GET['search'].encode('utf8')
        bing_url = "https://www.bing.com/search?" + urllib.urlencode({'q': result})
        zhihu_url="https://www.zhihu.com/search?type=content&"+urllib.urlencode({'q':result})
        dist = {
            'github': 'https://github.com/search?utf8=✓&' + urllib.urlencode({'q': result}),
            'google': "https://www.google.com/search?" + urllib.urlencode({'q': result}),
            'weibo': "http://s.weibo.com/weibo/" + str(result),
            'quora': "https://www.quora.com/search?" + urllib.urlencode({'q': result})

        }
        len_bing,bingr=bing(bing_url)
        len_zhi,zhir=zhihu(zhihu_url)
        return render(request,'result.html',{'len_bing':len_bing,'bing':bingr,'len_zhi':len_zhi,'zhihu':zhir,'sd':dist})

    return render(request,'index.html')

def bing(url):
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    headers = {'User-Agent': User_Agent}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html)
    content = soup.select('.b_algo h2')
    res=[]
    for i in content:
        item = re.findall('href="(.*?)" target="_blank">(.*?)</a>', str(i), re.S)
        if item:
            a={'ref':item[0][0],'des':item[0][1]}
            res.append(a)
        else:
            item=re.findall('href="(.*?)">(.*?)</a>', str(i), re.S)
            if item:
                a = {'ref': item[0][0], 'des': item[0][1]}
                res.append(a)
    return len(res),res
def zhihu(url):

    User_Agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    headers={'User-Agent':User_Agent}
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html=response.read()
    soup=BeautifulSoup(html)
    content=soup.select('.title')
    res=[]
    for i in content:
        item=re.findall('<a class="js-title-link" href="(.*?)" target="_blank">(.*?)</a>',str(i),re.S)
        if item:
            a={'ref':"http://www.zhihu.com"+str(item[0][0]),'des':item[0][1]}
            res.append(a)
    return len(res),res
