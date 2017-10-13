#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

def joinData():
    provdf = pd.read_excel(r'C:\Users\WEB_PC_X1\Desktop\aaa.xlsx',sheetname=[0,1], dtype='str')
    print(type(provdf[0]['手机'][0]))
    df = pd.merge(provdf[0], provdf[1],how='right',left_on='编号', right_on='编号')
    print(df)

if __name__ == '__main__':
    joinData()
