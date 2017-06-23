#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
from _codecs import encode
import os
import pandas as pd
from sqlalchemy import create_engine
# import pymysql
import codecs

'''
def getimage(url):
        ret = requests.get(url,verify = True)
        if ret.status_code == 200:
            end = url.rindex('/')
            setpoint = url.rindex('-') + 1
            pathname = './pic' + url[end:setpoint - 1] + '/'
            if not os.path.isdir(pathname):
                os.mkdir(pathname)
            with open(pathname+url[setpoint:], 'wb') as f:
                f.write(ret.content)
            print("GOT IT %s" %url[setpoint:])

def gethtmlimage(htmlurl):
    html = requests.get(htmlurl, verify = True)
    htmltext = html.text.encode(html.encoding).decode('utf8')
    urls = re.findall(r'<img src="(.*?)">', htmltext)
    for item in urls:
        getimage(item)

'''

'''
#bbsurls = list(map(lambda x: 'https://www.mumu59.com/htm/piclist%d/' %x, range(5,21)))
bbsurls = ['http://jzb.com/bbs/forum.php?mod=forumdisplay&fid=3220&typeid=6149&filter=typeid&typeid=6149&page=1']
for bbsitem in bbsurls:
    html = requests.get(bbsitem)
    htmltext = html.text.encode(html.encoding).decode('utf8')
    tipurls = re.findall(r'<!--<a href="(.*?)" target="_blank"  class="xst" title="', htmltext)
    print(tipurls)
#    tipurls = ['http://jzb.com/bbs/thread-4894771-1-1.html']
    for tipurl in tipurls:
        tiphtml = requests.get(tipurl)
        tiphtmltext = tiphtml.text.encode(tiphtml.encoding).decode('utf8')
        tiptitles = re.findall(r'<title>(.*?)</title>', tiphtmltext)[0]
#        print(tiptitles)
        tiptimes = re.findall(r'<em id="authorposton(.*?)">(.*?)</em>', tiphtmltext)
        print(tiptimes)
'''
'''
def getimage(url):
        ret = requests.get(url,verify = True)
        if ret.status_code == 200:
            end = url.rindex('/')
            setpoint = url.rindex('-') + 1
            pathname = './pic' + url[end:setpoint - 1] + '/'
            if not os.path.isdir(pathname):
                os.mkdir(pathname)
            with open(pathname+url[setpoint:], 'wb') as f:
                f.write(ret.content)
            print("GOT IT %s" %url[setpoint:])

def gethtmlimage(htmlurl):
    html = requests.get(htmlurl, verify = True)
    htmltext = html.text.encode(html.encoding).decode('utf8')
    urls = re.findall(r'<img src="(.*?)">', htmltext)
    for item in urls:
        getimage(item)

'''

'''
getTips这个函数是最先写的，当时有点偷懒，后续发现有点问题，没再用了。但是还是留他一条露脸的机会
'''


def getTips(url):
    html = requests.get(url)
    htmltext = html.text.encode(html.encoding).decode('utf8')
    with codecs.open('c:/工具//test//jzb.html', 'w', 'utf8') as f:
        f.write(htmltext)
    p_tips = r'target="_blank"  class="xst" title="(.+?)">'
    p_authors = r'.html" c="1">(.+?)</a></cite>'
    p_tiptimes = r'<em><span>(.+?)</span></em>\n</td>'
    p_tipurls = r'<!--<a href="(.+?)"'
    p_replys = r'<a href="http://jzb.com/bbs/thread-\d+-1-1.html" class="xi2">(\d+?)</a>'
    p_reads = r'</a><em>(\d+)</em></td>'
    pat_tips = re.compile(p_tips)
    pat_authors = re.compile(p_authors)
    pat_tiptimes = re.compile(p_tiptimes)
    pat_tipurls = re.compile(p_tipurls)
    pat_replys = re.compile(p_replys)
    pat_reads = re.compile(p_reads)
    titles = re.findall(pat_tips, htmltext)
    authors = re.findall(pat_authors, htmltext)
    tiptimes = re.findall(pat_tiptimes, htmltext)
    tipurls = re.findall(pat_tipurls, htmltext)
    replys = re.findall(pat_replys, htmltext)
    reads = re.findall(pat_reads, htmltext)
    contact_tips = list(zip(titles, authors, tiptimes, tipurls, replys, reads))
    return contact_tips


def getTips2(url):
    html = requests.get(url)
    htmltext = html.text.encode(html.encoding).decode('utf8')
    p = r'<tbody id="normalthread_\d+">([\s\S]+?)</tbody>'
    pat = re.compile(p)
    tips = re.findall(pat, htmltext)
    tipinfo = []
    titles = []
    authors = []
    posttimes = []
    urls = []
    re_nums = []
    br_nums = []
    for tip in tips:
        # 获取每个帖子列表的HTML信息，存入threadname
        p_threadname = r'<span class="xst thread-name">([\s\S]+?)</span>'
        pat_threadname = re.compile(p_threadname)
        threadname = re.findall(pat_threadname, tip)
        # 获取帖子的URL信息，存入url
        p_url = r'</a>]</em> <a href="(.+?)" [target="_blank"|style="font-weight:]'
        pat_url = re.compile(p_url)
        url = re.findall(pat_url, threadname[0])
        # 获取帖子的标题信息，存入title
        p_title = r'target="_blank"  class="xst" title=".+?">(.+?)</a>\n'
        pat_title = re.compile(p_title)
        title = re.findall(pat_title, threadname[0])
        # 获取帖子的作者，存入author
        p_author = r'<a href="http://jzb.com/bbs/space-\d+.html" c="1">(.+?)</a></cite>'
        pat_author = re.compile(p_author)
        author = re.findall(pat_author, tip)
        # 获取帖子的发布时间，存入posttime
        p_pt = r'<em><span[ class="xi1"]*>(.+?)</span></em>'
        pat_pt = re.compile(p_pt)
        posttime = re.findall(pat_pt, tip)
        # 获取帖子的回复数量，存入re_num
        p_re = r'<td class="num"><a href="http://jzb.com/bbs/thread-\d+-1-\d+.html" class="xi2">(\d+?)</a><em>'
        pat_re = re.compile(p_re)
        re_num = re.findall(pat_re, tip)
        # 获取帖子的阅读数量，存入br_num
        p_br = r'</a><em>(\d+?)</em></td>'
        pat_br = re.compile(p_br)
        br_num = re.findall(pat_br, tip)
        tipinfo.append(list(zip(title, author, posttime, url, re_num, br_num)))
        titles.append(title)
        authors.append(author)
        posttimes.append(posttime)
        urls.append(url)
        re_nums.append(re_num)
        br_nums.append(br_num)
    df = pd.DataFrame({'title': titles,
                       'author': authors,
                       'posttime': posttimes,
                       'url': urls,
                       'num_reply': re_nums,
                       'num_read': br_nums})
    return df


if __name__ == "__main__":
    urls = list(map(lambda x: 'http://jzb.com/bbs/forum.php?mod=forumdisplay&fid=3220&typeid=6149&filter=typeid&typeid=6149&page=%d' % x,
                    range(1, 71)))
    df_tips = pd.DataFrame()
    for url in urls:
        df_tips = pd.concat([df_tips, getTips2(url)], ignore_index=True)
    df_tips.to_csv('./jzb.csv', encoding='utf8')
    # 这个数据库引擎老牛逼了，创建了个数据库引擎
    engine = create_engine('mysql+pymysql://%s:%s@%s/%s' % ('hsiaoguo', 'Qwerzxcv123', 'localhost', 'hsiaoguo'),
                           connect_args={'charset': 'utf8'})
    df_tips.to_sql('jzb', con = engine, if_exists = 'append', index = False)
