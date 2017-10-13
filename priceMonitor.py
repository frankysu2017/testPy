#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        headers = {"User-Agent":"Mozilla/12.0 (compatible; MSIE 8.0; Windows NT)"}
        r = requests.get(url, timeout=30, headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return "Error occurred @s %s" %e

def parsePage(itemlist, html):
    soup = BeautifulSoup(html, "html.parser")
    print(soup.find('body').prettify())

def printItemdPrice(itemlist):
    print("")

def main():
    url = 'https://item.taobao.com/item.htm?spm=a230r.1.14.10.ebb2eb2TSYfoX&id=549858741666&ns=1&abbucket=13#detail'
    html = getHTMLText(url)
    itemlist = []
    parsePage(itemlist, html)
    printItemdPrice(itemlist)

if __name__ == "__main__":
    main()
