#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pypinyin import pinyin, lazy_pinyin, Style
import pandas as pd
from functools import reduce


def nametopinyin(name):
    return ''.join(lazy_pinyin(name)).upper()


def zuhe(list1, list2):
    return [str1+'|'+str2 for str1 in list1 for str2 in list2]


def pinyin_2_hanzi(pinyinList):
    from Pinyin2Hanzi import DefaultDagParams
    from Pinyin2Hanzi import dag
    dagParams = DefaultDagParams()
    result = dag(dagParams, pinyinList, path_num=500000, log=True)#10代表侯选值个数
    return [''.join(item.path) for item in result]
    #for item in result:
    #    socre = item.score
    #    res = item.path # 转换结果
    #    print(socre, res)


if __name__ == '__main__':
    '''
    姓名转所有拼音组合
    name_df = pd.read_csv(r'./card.csv')
    #name_df['pinyin'] = name_df['name'].apply(nametopinyin)
    name_pinyin = []
    for name in name_df['name']:
        py_list = pinyin(name, style=Style.NORMAL, heteronym=True)
        zuhe_list = [[name, item] for item in reduce(zuhe, py_list)]
        name_pinyin += zuhe_list
    pd.DataFrame(name_pinyin, columns=['name', 'pinyin']).to_csv(r'./pinyin.csv')
    '''
    #拼音转所有可能的汉字组合
    with open('./maoji.txt', 'w', encoding='utf8') as f:
        for item in pinyin_2_hanzi(['mao', 'ji']):
            f.write(item+'\n')

    with open('./jimao.txt', 'w', encoding='utf8') as f:
        for item in pinyin_2_hanzi(['ji', 'mao']):
            f.write(item+'\n')