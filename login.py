#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re
from functools import reduce

def isPwdOK(password):
    '验证密码是否合规'
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

def register():
    '新用户注册'
    if not os.path.exists(r'./userdata'):
        with open(r'./userdata', 'w') as f:
            f.write('{}')
    with open(r'./userdata', 'r') as f:
        if bool(f.read()):
            f.seek(0, 0)
            userdata = json.load(f)
        else:
            userdata = {}
    username = input('Please input your username:\n')
    while username in userdata:
        username = input('%s has already registered, try another one:\n' %username)
    else:
        password = input('Please input your password:\n')
        while not isPwdOK(password):
            password = input('密码不符合规范，请重新输入：\n')
    userdata[username] = password
    with open(r'./userdata', 'w') as f:
        f.write(json.dumps(userdata))
    print('register successful')

def login():
    username = input('Please enter your username:\n')
    password = input('Please enter your password:\n')
    with open(r'./userdata', 'r') as f:
        userdata = json.load(f)
        while not ((username in userdata) and (userdata[username] == password)):
            print('login incorrect, please try again:')
            username = input('Please enter your username:\n')
            password = input('Please enter your password:\n')
        else:
            print('%s, welcome back' %username)

def menu():
    op = input('''Welcome to this Site!\n
          choose what do you want:\n
          [R]egister
          [L]ogin
          [E]xit
          ''')
    while op not in list('RLErle'):
        op = input('Please choose "R" or "L" or "E", sb!:\n')
    else:
        op  = op.upper()
        if op == 'R':
            register()
        elif op == 'L':
            login()
        else:
            print('Bye Bye')

if __name__ == '__main__':
    menu()