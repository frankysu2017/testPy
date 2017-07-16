#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bs4
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return "Error occurd @s %s" %e

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            ulist.append([tds[0].contents[0], tds[1].string, tds[2].string, tds[3].string])

def printUnivList(ulist, num):
    print("%10s\t%10s\t%10s\t%10s" %("排名", "学校名称", "省市", "总分"))
    for i in range(num):
        u = ulist[i]
        print("%10s\t%10s\t%10s\t%10s" %(u[0], u[1], u[2], u[3]))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)

if __name__ == "__main__":
    main()