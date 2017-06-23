#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv(r'./bbb.csv', sep = ',', names = ['id', 'name', 'phonelist'], header = None, dtype=str)
    df_new = pd.DataFrame([])
    for x in df.index:
        phones = df.ix[x]['phonelist'].split('，')
        for phone in phones:
            dict1 = {'id':df.ix[x]['id'],'name':df.ix[x]['name'],'phonelist':df.ix[x]['phonelist'],'phone':phone}
            df_new = df_new.append(dict1, ignore_index = True)
    print(df_new)