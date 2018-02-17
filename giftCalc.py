#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
from math import floor
from functools import reduce


class Goods(object):

    def __init__(self, index):
        __GOODSCODE__ = [181350, 178796, 118814, 120676, 207246, 206534, 131816, 16102, 86328, 175181, 41582, 92303,
                 119580, 177007, 138863, 108479, 105121, 71349, 147559, 168826, 173608, 204050, 204051, 213000,
                 216438, 188540, 184898, 204538, 202898, 117102, 148146, 210086, 109249, 115133, 203504, 139608,
                 217079, 219350, 179019, 126714, 126718, 144100, 144101, 144102, 174318, 210158, 217450, 3855, 153836,
                 180211, 999991, 999992, 999995]
        __GOODSNAME__ = ['德清源安心生态鲜鸡蛋礼盒60枚装2580g', '正大鸡蛋60枚', '百年栗园鸡蛋60枚', '晓仙白洋淀柴鸡蛋60枚3000g',
                '百年栗园散养柴鸡蛋48枚礼盒装2.06kg', '千禧农柴鸡蛋礼盒60枚2.75kg', '晓仙白洋淀柴鸡蛋40枚2000g',
                '5.436鲁花花生油', '5L鲁花花生油', '鲁花压榨特香菜籽油5L', '鲁花压榨一级花生油2.5L', '5L多力葵花籽油',
                '5L长寿花花生油', '欣奇曲有机亚麻籽油700ml', '贝蒂斯特级初榨橄榄没750ml', '多力芥花油5L',
                '阿格利司纯橄榄没1L', '河套雪花粉5kg', '金龙鱼多用途麦芯粉5kg', '金沙河高筋特精粉5kg', '古船麦心粉5kg',
                '五得利尚品麦芯粉5kg', '五德利金富强高筋小麦粉5kg', '金沙河松鹤贵族精粉5kg', '一加一天然面粉5kg',
                '隆福源五常稻花香5kg', '福临门稻花香5kg', '福临门辽河玉晶香5kg', '福临门三江家宴米5kg', '古船泰国香米5kg',
                '古船长粒大米5kg', '福临门宁夏宁府御贡米5kg', '蒙牛特仑苏纯牛奶250ml*12', '伊利金典纯牛奶250毫升*12',
                '伊利金典低脂纯牛奶250ml*12', '三元极致低脂纯牛奶250ml*12', '认养一头年纯牛奶250ml*12', '安佳卓冉高蛋白阳光奇异果牛奶250ml*10',
                '蒙牛纯甄牛奶礼盒200g*12', '佳诚富贵团圆礼盒2.306kg', '佳诚吉祥如意礼盒2.166kg', '万佳利加州原野快乐万家干果礼盒1.5kg',
                '万佳利加州原野茗果世界精选干果礼盒2.158kg', '万佳利加州原野福贵年年礼盒2.188kg', '万佳利加州原野锦绣年华礼盒1.535kg',
                '果园老农添香礼盒1.56kg', '芭提娅果汁礼盒1L*4', '露露杏仁露240ml', '养元六个核桃核桃乳240ml', '养元六个核桃无糖型核桃乳240ml',
                '10元超市券', '20元超市券', '50元超市券']
        __GOODSPRICE__ = [86, 84, 70, 59.9, 59.9, 59.9, 49.8, 149.9, 139, 85.9, 74.9, 69.9, 99, 139, 129, 82.9, 74,
                  95, 29.9, 29, 38, 46, 28.5, 38.9, 39, 105, 88, 36, 45, 75, 52, 36, 60, 60, 50, 49, 42, 82,
                  56, 199, 148, 198, 168, 178, 228, 199, 78, 79, 68, 95, 10, 20, 50]
        #__GOODSNUM__ = len(__GOODSCODE__)

        self.code = __GOODSCODE__[index]
        self.name = __GOODSNAME__[index]
        self.price = __GOODSPRICE__[index]
        self.num = len(__GOODSCODE__)

    def show_goods(self, file=None):
        print("name: {:30}, code: {:^10}, price: {:^6}".format(self.name, self.code, self.price), file=file)


def calctotalprice(goodslist):
    return reduce(lambda x, y: x+y, map(lambda x: x.price, goodslist))


def getgoodsindex(goods):
    __GOODSCODE__ = [181350, 178796, 118814, 120676, 207246, 206534, 131816, 16102, 86328, 175181, 41582, 92303,
                     119580, 177007, 138863, 108479, 105121, 71349, 147559, 168826, 173608, 204050, 204051, 213000,
                     216438, 188540, 184898, 204538, 202898, 117102, 148146, 210086, 109249, 115133, 203504, 139608,
                     217079, 219350, 179019, 126714, 126718, 144100, 144101, 144102, 174318, 210158, 217450, 3855,
                     153836, 180211, 999991, 999992, 999995]
    return __GOODSCODE__.index(goods.code)



'''
class Goods(object):
    def __init__(self, code=None, name=None, price=None):
        self.code = code
        self.name = name
        self.price = price


class Node(object):
    def __init__(self, account=0, goods=None):
        self.account = account
        self.goods = goods
        self.child_list = []

    def add_child(self, node):
        self.child_list.append(node)

    def add_children(self, nodelist):
        self.child_list.extend(nodelist)

    def show(self):
        print('account:%d' %self.account, end='--')
        if self.goods.name:
            print('code:%d' %self.goods.code, end='--')
            print('name:%s' %self.goods.name, end='--')
            print('price:%d' %self.goods.price)
        else:
            print('have no goods in the bag yet')


def goods_list(account):
    num, code, name, price = loaddata()
    account_list = []
    for i in range(num):
        if price[i] <= account:
            account_list.append(Node(account=account-price[i], goods=Goods(code=code[i],name=name[i],price=price[i])))
    return account_list


def create_tree(node=None):
    if node.account >= 10:       #the node's account can afford the cheapest goods at least
        for item in goods_list(node.account):
            node.add_child(create_tree(item))
            #print(item.goods.name)
        return node


def bagCalc(account=500, bag=[], total=0, start=0):
    num, code, name, price = loaddata()
    if account >= 10:
        for i in range(num):
            if account >= price[i]:
                bag.append((code[i], name[i]))
                account = account - price[i]
                total = total + price[i]
                print(bag, account)
                bagCalc(account, bag, total, i)
            else:
                continue
    else:
        start = start + 1
        bagCalc(500,[],start)
    return bag

def queryBag():
    pass
'''


'''
def count_one(bin_list):
    count = 0
    for i in bin_list:
        if i == 1:
            count += 1
    return count


def count_money(bin_list):
    num, code, name, price = loaddata()
    ext_price = []
    ext_code = []
    ext_name = []
    for i in range(num-3):
        n = floor(500/price[i])
        ext_price.extend([price[i]]*n)
        ext_code.extend([code[i]]*n)
        ext_name.extend([name[i]]*n)
    amount_list = list(map(lambda x, y: x*y, bin_list, ext_price))
    amount = reduce(lambda x, y: x+y, amount_list)
    return amount


def show_list(bin_list, file):
    num, code, name, price = loaddata()
    ext_price = []
    ext_code = []
    ext_name = []
    for i in range(num):
        n = floor(500/price[i])
        ext_price.extend([price[i]]*n)
        ext_code.extend([code[i]]*n)
        ext_name.extend([name[i]]*n)

    amount_list = list(map(lambda x, y: x*y, bin_list, ext_name))
    lst = []
    for item in amount_list:
        if len(item) > 0:
            lst.append(item)
    print(lst, end="\t:  ", file=file)


def calc2():
    num, code, name, price = loaddata()
    count = reduce(lambda x, y: x+y, [floor(500/i) for i in price])
    print(count)
    lst = []
    f = open(r'cutline.txt', 'w')
    for i in range(1, pow(2,361)):
        temp = list(str(bin(i)).replace('0b', '').zfill(361))
        temp = list(map(lambda x: int(x), temp))
        if count_one(temp) <= 50:
            if 450 < count_money(temp) <= 500:
                #print('got one!')
                show_list(temp, f)
                print(count_money(temp), file=f)
    f.close()
'''


if __name__ == '__main__':
    alllist = []
    for i in range(53):
        alllist.append([Goods(i)])
    flag = 1
    f = open(r'cutline.txt', 'w')
    while flag == 1:
        count = 0
        templist = []
        for glist in alllist:
            flag = 0
            index = getgoodsindex(glist[-1])
            for i in range(index, 53):
                newlist = glist.copy()
                newlist.append(Goods(i))
                listprice = calctotalprice(newlist)
                if listprice <= 500:
                    flag = 1
                    templist.append(newlist)
                    if listprice > 490:
                        count += 1
                        for goods in newlist:
                            goods.show_goods(file=f)
                        print('total: %0.1f---------------------------------------------' %listprice, file=f)
        alllist = templist.copy()
        print(len(alllist),  end='\t\t')
        print(count)
    f.close()
