#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import os
from bs4 import BeautifulSoup as bs
from functools import reduce
import multiprocessing

'''
通过URL获取JPG图片
'''
def getimage(url, titles):
    imghtml = requests.get(url,verify = True)
    if imghtml.status_code == 200:
        end = url.rindex('/')
        setpoint = url.rindex('-') + 1
        pathname = './pic/' + titles + '/' #url[end:setpoint - 1] + '/'
        if not os.path.isdir(pathname):
            os.mkdir(pathname)
        with open(pathname+url[end:], 'wb') as f:
            f.write(imghtml.content)
        print("GOT IT %s" %url[setpoint:])
'''
调用getimage()函数，获取一个网页中所有的照片，采用多进程同时抓取网页中所有的照片
'''

def gethtmlimage(htmlurl, titles):
    html = requests.get(htmlurl, verify = True)
    htmltext = html.text.encode(html.encoding).decode('utf8')
    urls = re.findall(r'<img src="(https://img.+?.[jpg|png])">', htmltext)
    '''
    pool = multiprocessing.Pool(50)
    pool.map(getimage, urls, titles)
    pool.close()
    '''
    p_l = []
    for item in urls:
        p_l.append(multiprocessing.Process(target=getimage, args=(item,titles)))
    for p in p_l:
        p.start()

'''
调用gethtmlimage()函数，获取一个论坛版块中所有帖子里的图片
'''
def getTipurls(securllist):
    tipurllist = []  #每个帖子的url列表
    for securl in securllist:
        html = requests.get(securl, verify = True)
        htmltext = html.text.encode(html.encoding).decode('utf8')
        pat = r'<li><a href="(/htm/pic\d/\d+?.htm)" target="_blank"><span>\d{2}-\d{2}</span>(.*?)</a></li>'
        tup = re.findall(pat, htmltext)
        setpoint = securl.index('.com/') + 4
        templist = list(map(lambda x: (securl[:setpoint] + x[0], x[1]), tup))
        tipurllist.extend(templist)
        #print((tipurllist))
        for item in tipurllist:
            gethtmlimage(item[0], item[1])

'''
判断输入的要求是否合法
'''
def checkInput(sec_input):
    sec_list = sec_input.split('|')
    checklist = list(map(lambda x: re.match('^[0-46-9]$', x), sec_list))
    return bool(reduce(lambda x, y: x and y, checklist))

if __name__ == "__main__":
    sec_input = input('请输入你想抓取的版块，如果是多个版块，请用"|"分隔（例如：1|3|6）：                               \n[1]自拍偷拍\n[2]亚洲色图\n[3]欧美色图\n[4]美腿丝袜\n[6]清纯唯美\n[7]乱伦熟女\n[8]卡通动漫\n')
    while(not checkInput(sec_input)):
        sec_input = input('选择有误，请重新选择：')
    print('输入正确！真TM不容易-_-#')
    sec_list = sec_input.split('|')
    sec_list = list(map(lambda x: 'https://www.hhh310.com/htm/piclist%s/' %x, sec_list))
    securllist = []
    pages = list(range(1,6))  #默认每个版块抓取前十页
    for section in sec_list:
        pageurls = list(map(lambda x: section + '%d.htm' %x, pages))
        securllist.append(pageurls)
    for pageurl in securllist:
        getTipurls(pageurl)
