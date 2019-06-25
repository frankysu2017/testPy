#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tabula

if __name__ == '__main__':
    df = tabula.read_pdf(r'./test.pdf', encoding='gbk', pages='all', output_format ='json', area=[0,30,9 0,105])
    print(df)
    for item in df[0]['data']:
        for dic in item:
            print(dic['text'], end=', ')
        print()
    df.to_csv(r'./test.csv')