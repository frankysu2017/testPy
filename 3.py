#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@uthor: Wang
D@te: 2018-6-18
'''

if __name__ == '__main__':
    a=eval(input('山的高度：\n'))

    b = 0.0001  # 纸的厚度
    n = 0       # 折叠次数
    while b <= a:
        b = b * 2
        n=n+1
    print(n)
