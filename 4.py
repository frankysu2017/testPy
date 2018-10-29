#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@uthor: Wang
D@te: 2018-6-18
'''

if __name__ == '__main__':
    a = 0
    while a <= 0 or a >= 300:
        a=int(input('输入整数N（N<300)\n'))
    for i in range(1,a+1):
        if i%7 == 0 or i%10 == 7:
            print(i)

