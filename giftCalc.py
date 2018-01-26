#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def loadData():
    GoodsNum = 53
    GoodsCode = [181350, 178796, 118814,120676, 207246, 206534, 131816, 16102, 86328, 175181, 41582, 92303,
                 119580, 177007, 138863, 108479, 105121, 71349, 147559, 168826, 173608, 204050, 204051, 213000,
                 216438, 188540, 184898, 204538, 202898, 117102, 148146, 210086, 109249, 115133, 203504, 139608,
                 217079, 219350, 179019, 126714, 126718, 144100, 144101, 144102, 174318, 210158, 217450, 3855, 153836,
                 180211, 999991, 999992, 999995]
    GoodsName = ['德清源安心生态鲜鸡蛋礼盒60枚装2580g', '正大鸡蛋60枚', '百年栗园鸡蛋60枚', '晓仙白洋淀柴鸡蛋60枚3000g',
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
    GoodsPrice = [86, 84, 70, 59.9, 59.9, 59.9, 49.8, 149.9, 139, 85.9, 74.9, 69.9, 99, 139, 129, 82.9, 74,
                  95, 29.9, 29, 38, 46, 28.5, 38.9, 39, 105, 88, 36, 45, 75, 52, 36, 60, 60, 50, 49, 42, 82,
                  56, 199, 148, 198, 168, 178, 228, 199, 78, 79, 68, 95, 10, 20, 50]
    return GoodsNum, GoodsCode, GoodsName, GoodsPrice


def bagCalc(account=500, bag=[], total=0, start=0):
    num, code, name, price = loadData()
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

def goodsfilter(account):
    num, code, name, price = loadData()
    goodslist = []
    for i in range(num):
        if price[i] <= account:
            goodslist.append([code[i], name[i], account - price[i]])
    return goodslist


if __name__ == '__main__':
    purse = 500
    bags = goodsfilter(purse)
    print(bags)
    print('------------------------------------')
    for list in goodsfilter(purse):
        purse = list[2]
        print(list[1], end=' + ')
        while purse >= 10:
            list2 = goodsfilter(purse)[0]
            purse = list2[2]
            name = list2[1]
            print(name, end=' + ')
        print('')
