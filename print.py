#!/usr/bin/env python3
# coding: utf-8

import json
import pandas as pd
from sqlalchemy import create_engine
from numpy import random
from math import isnan
import gc
from hashlib import sha3_256, md5
import re

def countPhones(phones):
    if phones != phones:    #表示phone字段是
        return 0
    else:
        return len(phones.split(';'))


if __name__ == "__main__":
    #连接MySQL数据库
    user = 'hsiaoguo'
    password = 'Qwerzxcv123'
    server = 'localhost'
    dbname = 'flask'
    engine = create_engine('mysql+pymysql://%s:%s@%s/%s' %(user, password, server, dbname), connect_args={'charset':'utf8'})
    with open(r'/Users/junie/PycharmProjects/testPy/abc.txt', 'r', encoding='utf8') as f:
        j1 = json.load(f)
        data = pd.DataFrame.from_dict(j1['response']['docs'])
        f = lambda x: md5(str(x.values).encode('utf8')).hexdigest()
        dHash = data.apply(f, axis=1)
        data['uhash'] = dHash
        data = data.set_index('uhash', drop=False, verify_integrity=True)

        #这个是把pandas的一行展开成多行的操作，网上抄来的，感觉很牛逼的样子，貌似那个stack()是个神来之笔
        dfPhone = pd.DataFrame(data['phone'].str.split(';', expand=True).stack().reset_index(level=1, drop=True),columns=['phone'])

        #把字符串里的非数字都去掉，以便统一电话格式
        f1 = lambda x: re.sub('\D', '', x)

        dfPhone['phone'] = dfPhone['phone'].apply(f1)
        dfPhone['uhash'] = dfPhone.index
        data.to_sql('idens', con=engine, if_exists='append', index=False)
        dfPhone.to_sql('phones', con=engine, if_exists='append', index=False)  # append|fail|replace
