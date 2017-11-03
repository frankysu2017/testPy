#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import multiprocessing

def getText(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/50.0.2661.102'}
    html = requests.get(url, verify=True, headers=header)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text.encode(html.encoding).decode('utf8'), 'lxml')
        filename = './novel/' + soup.title.string.split(' - ')[0] + '.txt'
        toWrite = soup.body.find('div', class_="novelContent")
        with open(filename, 'w', encoding='gbk') as f:
            f.write(str(toWrite.text))

def getList(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/50.0.2661.102'}
    html = requests.get(url, verify=True, headers=header)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text.encode(html.encoding).decode('utf8'), 'lxml')
        list = soup.find_all('a', target='_blank')
        siteUrl = url[:url.index('.com')+4]
        novelUrl = map(lambda x: siteUrl+x.get('href'), list)
        #for item in novelUrl:
        #    print(item)
        return novelUrl

if __name__ == "__main__":
    urls = [r'https://www.uuu711.com/htm/novellist5/'+str(x+1)+r'.htm' for x in range(200)]
    for url in urls:
        SpiderList = []
        getList(url)
        for item in getList(url):
            SpiderList.append(multiprocessing.Process(target=getText, args=(item, )))
        for proc in SpiderList:
            proc.start()