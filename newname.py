#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
import ast

#数理:1、2为木；3、4为火；5、6为土；7、8为金；9、10为水
shuli = ['水', '木', '木', '火', '火', '土', '土', '金', '金', '水']
wuxing = {"木木木": "大吉", "木木火": "大吉", "木木土": "大吉", "木木金": "凶多吉少", "木木水": "吉多于凶", "木火木": "大吉", "木火火": "中吉", "木火土": "大吉", "木火金": "凶多于吉", "木火水": "大凶", "木土木": "大凶", "木土火": "中吉", "木土土": "吉", "木土金": "吉多于凶", "木土水": "大凶", "木金木": "大凶", "木金火": "大凶", "木金土": "凶多于吉", "木金金": "大凶", "木金水": "大凶", "木水木": "大吉", "木水火": "凶多于吉", "木水土": "凶多于吉", "木水金": "大吉", "木水水": "大吉", "火木木": "大吉", "火木火": "大吉", "火木土": "大吉", "火木金": "凶多于吉", "火木水": "中吉", "火火木": "大吉", "火火火": "中吉", "火火土": "大吉", "火火金": "大凶", "火火水": "大凶", "火土木": "吉多于凶", "火土火": "大吉", "火土土": "大吉", "火土金": "大吉, ""火土水""吉多于凶", "火金木": "大凶", "火金火": "大凶", "火金土": "吉凶参半", "火金金": "大凶", "火金水": "大凶", "火水木": "凶多于吉", "火水火": "大凶", "火水土": "大凶", "火水金": "大凶", "火水水": "大凶", "土木木": "中吉", "土木火": "中吉", "土木土": "凶多于吉", "土木金": "大凶", "土木水": "凶多于吉", "土火木": "大吉", "土火火": "大吉", "土火土": "大吉", "土火金": "吉多于凶", "土火水": "大凶", "土土木": "中吉", "土土火": "大吉", "土土土": "大吉", "土土金": "大吉", "土土水": "凶多于吉", "土金木": "凶多于吉", "土金火": "凶多于吉", "土金土": "大吉", "土金金": "大吉", "土金水": "大吉", "土水木": "凶多于吉", "土水火": "大凶", "土水土": "大凶", "土水金": "吉凶参半", "土水水": "大凶", "金木木": "凶多于吉", "金木火": "凶多于吉", "金木土": "凶多于吉", "金木金": "大凶", "金木水": "凶多于吉", "金火木": "凶多于吉", "金火火": "吉凶参半", "金火土": "吉凶参半", "金火金": "大凶", "金火水": "大凶", "金土木": "中吉", "金土火": "大吉", "金土土": "大吉", "金土金": "大吉", "金土水": "吉多于凶", "金金木": "大凶", "金金木": "大凶", "金金土": "大吉", "金金金": "中吉", "金金水": "中吉", "金水木": "大吉", "金水火": "凶多于吉", "金水土": "吉", "金水金": "大吉", "金水水": "中吉", "水木木": "大吉", "水木火": "大吉", "水木土": "大吉", "水木金": "凶多于吉", "水木水": "大吉", "水火木": "中吉", "水火火": "大凶", "水火土": "凶多于吉", "水火金": "大凶", "水火水": "大凶", "水土木": "大凶", "水土火": "中吉", "水土土": "中吉", "水土金": "中吉", "水土水": "大凶", "水金木": "凶多于吉", "水金火": "凶多于吉", "水金土": "大吉", "金金": "中吉", "水金水": "大吉", "水水木": "大吉", "水水火": "大凶", "水水土": "大凶", "水水金": "大吉", "水水水": "中吉"}
f = open(r'81sl.txt', 'r')
shuli81 = ast.literal_eval(f.read())
f.close()
f = open(r'shui.txt', 'r')
shui = f.read().split(",")
f.close()
kangxibihua = {}
f = open(r'kangxibihua.txt', 'r')
for line in f:
    line = line.split(":")
    bihua = int(line[0])
    string = line[1]
    for item in string:
        kangxibihua[item] = bihua
del kangxibihua['\n']


def getxingmingxue(name):
    url = r'http://www.name321.net/zidian/zidian.htm'
    driver = wd.Chrome()
    driver.get(url)
    driver.find_element_by_name(r'hz').send_keys(name)
    driver.find_elements_by_class_name('input1')[0].click()
    html = driver.page_source
    soup = bs(html, 'lxml').find_all(attrs={'class': 'left'})
    find = re.findall(r'\[姓名学] 笔划:(\d+)； 五行:(.+)<br/>', str(soup))
    if find:
        bihua, wuxing = find[0]
    else:
        return 1000, '全'

    #traditional = re.findall(r'\[繁体笔划] \((.+):', str(soup))[0]

    return int(bihua), wuxing      #, traditional


def wugesancai(name):
    name = name.split('|')
    xing = name[0]
    ming = name[1]

    xing = [getxingmingxue(charc) for charc in xing]
    ming = [getxingmingxue(charc) for charc in ming]


    # 姓名五行
    xingwuxing = [item[1] for item in xing]
    mingwuxing = [item[1] for item in ming]
    namewuxing = "".join(xingwuxing) + "".join(mingwuxing)
    print(namewuxing, wuxing.get(namewuxing))


    xing = [item[0] for item in xing]
    ming = [item[0] for item in ming]

    # 计算天格
    if len(xing) == 1:
        tiange = xing[0] + 1
    elif len(xing) == 2:
        tiange = xing[0] + xing[1]
    else:
        tiange = 100

    # 计算人格
    renge = xing[-1] + ming[0]

    #计算地格
    if len(ming) == 1:
        dige = ming[0] +1
    else:
        dige = sum(ming)

    #计算外格
    waige = sum(xing) + sum(ming) - renge
    if len(xing) == 1:
        waige = waige +1
    if len(ming) == 1:
        waige = waige + 1

    #计算总格
    zongge = sum(xing) + sum(ming)

    #计算三才
    sancai = [tiange%10, renge%10, dige%10]
    sancai = [shuli[i] for i in sancai]
    sancai = "".join(sancai)

    return tiange, renge, dige, waige, zongge, sancai


def getname(numlist):
    tiange = 16
    renge = 15 + numlist[0]
    dige = sum(numlist)
    waige = 15 + sum(numlist) - renge + 1
    zongge = 15 + sum(numlist)
    return tiange, renge, dige, waige, zongge


if __name__ == "__main__":
    '''
    name = input('请输入您的姓名，用|分开（如：李|天一，司马|懿）：\n')
    while '|' not in name:
        print('傻叉，名字没写对！')
        name = input('请输入您的姓名，用|分开（如：李|天一，司马|懿）：\n')
    tiange, renge, dige,waige, zongge, sancai = wugesancai(name)
    print(tiange, renge, dige, waige, zongge)
    print("天格%d: %s" % (tiange, shuli81.get(tiange)))
    print("人格%d: %s" % (renge, shuli81.get(renge)))
    print("地格%d: %s" % (dige, shuli81.get(dige)))
    print("外格%d: %s" % (waige, shuli81.get(waige)))
    print("总格%d: %s" % (zongge, shuli81.get(zongge)))
    print("三才:%s, %s" % (sancai, wuxing.get(sancai)))
    '''

    '''
    for item in shui:
        bihua = getxingmingxue(item)[0]+15
        if bihua in jilist:
            print(bihua, item)
    16 34 31 13 46
    '''

    jilist = [1,3,5,6,7,11,13,15,16,21,23,24,29,31,32,33,35,37,41,45,47,48,52,57,61,63,65,67,68,81]
    numlist = [[i, j] for i in range(1,40) for j in range(1,40)]
    for item in numlist:
        tiange, renge, dige, waige, zongge = getname(item)
        if (tiange in jilist) and (renge in jilist) and (dige in jilist) and (waige in jilist) and (zongge in jilist):
            isji = wuxing.get('土'+shuli[renge%10]+shuli[dige%10])
            if isji == '大吉':
                print(item, isji, tiange, renge, dige, waige, zongge)
