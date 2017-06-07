#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from functools import reduce

'''
数字清洗中经常预见很多不正常的字符如连续的‘aaaaaa'、‘1q2w3e4r'等等，用这个isPwdOK去判断
'''
def isPwdOK(password):
    if(len(password) < 4):
        print('太短！要超过4位！')
        return False;
    else:
        p = r'([\w ])\1{3}' #重复的数字字母或空格
        if (re.search(p, password) != None):
            print('重复！')
            return False;
        else:
            #指定一些常用连续字母、数字
            str1 = '01234567890'
            str2 = '09876543210'
            str3 = 'abcdefghijklmnopqrstuvwxyz'
            str4 = str2.upper()
            str5 = 'qwertyuiopasdfghjklzxcvbnm'
            str6 = str5.upper()
            str_arr = [str1, str2, str3, str4, str5, str6]
            str_num = re.findall(r'\d+', password)
            str_num = ''.join(str_num)
            str_chac = re.findall(r'[a-zA-Z]+', password)
            str_chac = ''.join(str_chac)
            match_num = list(map(lambda x: re.search(str_num, x) == None, str_arr))
            match_chac = list(map(lambda x: re.search(str_chac, x) == None, str_arr))
            numOK = bool(reduce(lambda x, y: x and y, match_num))
            chacOK = bool(reduce(lambda x, y: x and y, match_chac))
            return numOK or chacOK
if __name__ == '__main__':
    str_in = input('输入密码：\n')
    while(not isPwdOK(str_in)):
        str_in = input('密码不符合规范，请重新输入：\n')
    print('这就可以了！')
