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
        #setpoint = url.rindex('-') + 1
        pathname = './BBS/pic/' + titles + '/'
        if not os.path.isdir(pathname):
            os.mkdir(pathname)
        with open(pathname+url[end:], 'wb') as f:
            f.write(imghtml.content)
        print("GOT IT %s%s" %(titles, url[end:]))
'''
调用getimage()函数，获取一个网页中所有的照片，采用多进程同时抓取网页中所有的照片
'''

def gethtmlimage(htmlurl, titles):
    html = requests.get(htmlurl, verify = True)
    htmltext = html.text.encode(html.encoding).decode('utf8')
    soup = bs(htmltext, 'lxml').html.body.div.main
    urls = [x['data-original'] for x in soup.find(name='div', attrs={'class': 'content'}).find_all(name='img')]
    '''
    soup = bs(htmltext, 'lxml').html.body.div.main.div.next_sibling.next_sibling.next_sibling.next_sibling
    urls = [x['data-original'] for x in soup.find_all('img')]    
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
        soup = bs(htmltext, 'lxml').html.body.div.main
        tipurllist = [(r'https://www.797yt.com'+x.a['href'], x.a['title']) for x in soup.find_all(name='li')]
        '''
        soup = bs(htmltext, 'lxml').html.body.div.main.div.next_sibling.next_sibling.div.next_sibling.next_sibling.div
        tipurllist = [(r'https://www.797yt.com'+x.a['href'], x.a['title']) for x in soup.find_all('li')]
        '''
        #print(tipurllist)
        for item in tipurllist:
            gethtmlimage(item[0], item[1])


'''
判断输入的要求是否合法
'''
def checkInput(sec_input):
    sec_list = sec_input.split('|')
    checklist = list(map(lambda x: re.match('^[1-7]$', x), sec_list))
    return bool(reduce(lambda x, y: x and y, checklist))

if __name__ == "__main__":

    sec_input = input('请输入你想抓取的版块，如果是多个版块，请用"|"分隔（例如：1|3|6）：'
                      '                               \n[1]自拍偷拍\n[2]亚洲色图\n[3]欧美色图\n[4]美腿丝袜\n[5]清纯唯美\n[6]乱伦熟女\n[7]卡通动漫\n')
    sec_name = ['自拍偷拍', '亚洲色图', '欧美色图', '美腿丝袜', '清纯唯美', '乱伦熟女', '卡通动漫']
    while(not checkInput(sec_input)):
        sec_input = input('选择有误，请重新选择：')
    print('输入正确！真TM不容易-_-#')
    sec_list = sec_input.split('|')
    sec_list = list(map(lambda x: 'https://www.797yt.com/tupian/list-%s-' %sec_name[int(x)-1], sec_list))
    securllist = []
    pages = list(range(1, 2))  #默认每个版块抓取前十页
    for section in sec_list:
        pageurls = list(map(lambda x: section + '%d.html' %x, pages))
        securllist.append(pageurls)
    for pageurl in securllist:
        getTipurls(pageurl)
