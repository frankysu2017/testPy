#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    '''
    rest = -1
    while rest < 0:
        a = 0
        while a<1 or a>10:
            a = int(input('请输入钢笔的数量（1-10）\n'))
        b = 0
        while b<1 or b>30:
            b = int(input('请输入本子的数量（1-30）\n'))
        rest = 150 - a*13 - b*4
        if rest >= 0:
            print('剩余%d元' %rest)
        else:
            print('预算超支，重新输入\n')
    '''
    fnew = open(r'c:\19.txt', 'w')
    with open(r'c:\18.txt', 'r') as f:
        for line in f:
            fnew.write(line.replace(':', ';'))
    fnew.close()
