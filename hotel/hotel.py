#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
from functools import reduce
import time
import datetime


def is_valid_date(date_str):
    if len(date_str) == 8:
        try:
            time.strptime(date_str, "%Y%m%d")
            return True
        except:
            return False
    elif len(date_str) == 6:
        try:
            time.strptime(date_str, "%y%m%d")
            return True
        except:
            return False
    else:
        return False


def idVerify(id_str):
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    validate = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    id = list(id_str)

    if not id_str[:17].isdigit():
        return id_str, False

    if len(id_str) == 17:
        if is_valid_date(id_str[6:14]):
            multi_weight = list(map(lambda x, y: x*int(y), weight, id))
            validate_serial = reduce(lambda x, y: x+y, multi_weight) % 11
            return id_str+validate[validate_serial], True
        else:
            return id_str, False

    elif len(id_str) == 18:
        if is_valid_date(id_str[6:14]):
            multi_weight = list(map(lambda x, y: x * int(y), weight, id[:-1]))
            validate_serial = reduce(lambda x, y: x + y, multi_weight) % 11
            if validate[validate_serial] == id[-1]:
                return id_str, True
            else:
                return id_str, False
        else:
            return id_str, False

    elif len(id_str) == 15:
        if is_valid_date(id_str[6:12]):
            if int(id_str[6:8]) <= int(str(datetime.datetime.now().year)[2:]):
                id_str = id_str[:6] + '20' + id_str[6:]
            else:
                id_str = id_str[:6] + '19' + id_str[6:]
            return idVerify(id_str)
        else:
            return id_str, False
    else:
        return id_str, False


def precess_data(str):
    column_dict = {'Name': 0, 'CardNo': 1, 'Descriot': 2, 'CtfTp': 3, 'CtfId': 4, 'Gender': 5, 'Birthday': 6,
                   'Address': 7, 'Zip': 8, 'Dirty': 9, 'District1': 10, 'District2': 11, 'District3': 12,
                   'District4': 13, 'District5': 14, 'District6': 15, 'FirstNm': 16, 'LastNm': 17, 'Duty': 18,
                   'Mobile': 19, 'Tel': 20, 'Fax': 21, 'EMail': 22, 'Nation': 23, 'Taste': 24, 'Education': 25,
                   'Company': 26, 'CTel': 27, 'CAddress': 28, 'CZip': 29, 'Family': 30, 'Version': 31, 'id': 32}
    l = str.split(',')
    # 校验身份证，补齐至18位
    if idVerify(l[column_dict['CtfId']])[1]:
        l[column_dict['CtfId']] = idVerify(l[column_dict['CtfId']])[0]
        l[column_dict['CtfTp']] = "ID"
        l[column_dict['Birthday']] = l[column_dict['CtfId']][6:14]
        l[column_dict['Gender']] = "M" if int(l[column_dict['CtfId']][-2]) % 2 != 0 else "F"
    else:
        return str, False;
    return ",".join(l), True


if __name__ == '__main__':
    path = r'C:/如家数据/'
    result = open(r'./result.csv', 'w', encoding='utf8')
    error = open(r'./error.csv', 'w', encoding='utf8')
    doubt = open(r'./doubt.csv', 'w', encoding='utf8')
    column = 'Name,CardNo,Descriot,CtfTp,CtfId,Gender,Birthday,Address,' \
             'Zip,Dirty,District1,District2,District3,District4,District5,' \
             'District6,FirstNm,LastNm,Duty,Mobile,Tel,Fax,EMail,Nation,Taste,' \
             'Education,Company,CTel,CAddress,CZip,Family,Version,id'
    error.write(column)
    result.write(column)
    doubt.write(column)
    for filename in os.listdir(path):
        with open(path+filename, 'r', encoding='utf8') as f:
            next(f)
            for line in f:
                p = re.compile('"(.+?)"')
                l = re.findall(p, line)
                for item in l:
                    line = line.replace(item, item.replace(',', '，'))
                if line.count(',') != 32:
                    error.write(line)
                else:
                    line = line.replace("'", '').replace('"', '')
                    line, flag = precess_data(line)
                    if flag:
                        result.write(line)
                    else:
                        doubt.write(line)
    result.close()
    error.close()
    doubt.close()
    '''
    str = '曹晓龙,,,ID,效30103197401250518,M,19740125,-,-,,,CHN,-1,-1,,,,,,13308455170,-,-,caoxiaolong8888@126.com,,,,,,,,,,12452'
    print('效30103197401250518'[:-2])
    '''