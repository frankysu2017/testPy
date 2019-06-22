#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from random import randint
from math import sqrt
from random import randint
from socket import socket, SOCK_STREAM, AF_INET


def narcissistic():
    '''
    寻找“水仙花数”：三位数各位立方和等于原数字
    '''
    for i in range(100,1000):
        l = list(map(int, str(i)))
        sum = 0
        for item in l:
            sum += item ** 3
        if sum == i:
            print(i)


def perfectnumber():
    '''
    寻找“完美数”：所有真因子之和等于原数字
    '''
    for num in range(100000):
        sum = 0
        for x in range(1, num):
            if num%x == 0:
                sum += x
        if sum == num:
            print(sum)

def chickenpay():
    '''
    百鸡百钱问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何?
    '''
    for rouster in range(1, 100//5):
        for hen in range(1, 100//3):
            for chick in range(1, 100*3):
                if rouster*5 + hen*3 + chick/3 == 100:
                    print("%d * 5 + %d *3 + %d * 1/3 = 100;" %(rouster, hen, chick))


def fibonacci1(n):
    '''
    生成斐波那契数列：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
    采用递归的算法
    :return fn
    '''
    if n <= 0:
        return 0
    elif n == 1 or n ==2:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)


def fibonacci2(n):
    '''
    生成斐波那契数列：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
    采用python生成器，执行效率高的不要不要的
    :return fn
    '''
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a + b
        yield a


def craps(chip=1000):
    '''
    craps游戏规则：玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；
    如果点数和为2、3或12，则玩家输庄家胜。
    若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜。
    :param chip:筹码数量 > 0
    :return:
    '''
    while chip > 0:
        print("当前筹码为%d" % chip)
        n = int(input("请下注："))
        if n > chip:
            print("没那么多筹码了，帮你all in")
            n = chip
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        dicesum = dice1 + dice2
        print("第一局掷出%d点" % dicesum, end="----")
        if dicesum == 7 or dicesum == 11:
            print("玩家胜")
            chip += n
        elif dicesum in [2, 3, 12]:
            print("庄家胜")
            chip -= n
        else:
            print("平局，继续掷骰子")
            dice1 = randint(1, 6)
            dice2 = randint(1, 6)
            while dicesum != dice1 + dice2 or dice1 + dice2 !=7:
                print("掷出%d点" % (dice1+dice2), end="----")
                print("平局，继续掷骰子")
                dice1 = randint(1, 6)
                dice2 = randint(1, 6)
                if dice1 + dice2 == 7:
                    print("掷出7点，庄家胜")
                    chip -= n
                    break
                elif dice1 + dice2 == dicesum:
                    print("掷出第一局相同点数，玩家胜")
                    chip += n
                    break
        if chip > 0:
            print("游戏继续")
    print("恭喜你，输光啦！")


def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定IP地址和端口(端口用于区分不同的服务)
    # 同一时间在同一个端口上只能绑定一个服务否则报错
    server.bind(('localhost', 6789))
    # 3.开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器.')
        # 5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.断开连接
        client.close()


if __name__ == '__main__':
    #narcissistic()
    #perfectnumber()
    #chickenpay()
    '''
    start = datetime.now()
    for i in range(36):
        print(fibonacci1(i))
    end = datetime.now()
    print("递归方法归耗时%f秒" %(float((end-start).microseconds)/100000.0))

    start = datetime.now()
    for i in fibonacci2(35):
        print(i)
    end = datetime.now()
    print("生成器方法耗时%f秒" %(float((end-start).microseconds)/100000.0))
    '''
    #craps(1000)
    main()
