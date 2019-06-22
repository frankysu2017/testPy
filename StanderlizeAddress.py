#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
利用高德地图api实现地址和经纬度的转换
我的高德key: 895d8c6afa27ba2b57dd757ab490e16d
'''
import requests
import xlrd
import pandas as pd

def geocode(city, address):
    parameters = {'address': address, 'city': city, 'key': '895d8c6afa27ba2b57dd757ab490e16d'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    #print(response.json())
    answer = response.json()
    return answer

def get_station_name(filename):
    xlsbook = xlrd.open_workbook(filename)
    table = xlsbook.sheet_by_name('合并')
    station_list = table.col_values(0,1,)
    province_list = []
    for item in station_list:
        province_list.append(get_provice_abbr(get_geoinfo('%s站' % item)['province']))
    df = pd.DataFrame({'station': station_list, 'province': province_list})
    return df


def get_geoinfo(address, city = ''):
    j_geo = geocode(city, address)
    default_geo = {'formatted_address': '',
                   'country': '', 'province': '',
                   'citycode': '', 'city': '',
                   'district': '', 'township': [],
                   'neighborhood': {'name': [], 'type': []}, 'building': {'name': [], 'type': []},
                   'adcode': '', 'street': [], 'number': [],
                   'location': ',', 'level': ''}
    '''
    geo_dict字典格式
    'formatted_address'   #标准化地址
    'province'            #省
    'city'                #市
    'district'            #区
    'location'            #经度,纬度
    '''
    if j_geo['count'] == '1':
        return j_geo['geocodes'][0]
    else:
        return default_geo


#get the abbreviation of province. example:江苏省-->江苏，内蒙古自治区-->内蒙古
def get_provice_abbr(province):
    if len(province) == 0:
        return ''
    elif province[0] in ['黑', '内']:
        return province[:3]
    else:
        return province[:2]


if __name__=='__main__':
    #print(get_provice_abbr(get_geoinfo('通州', '')['province']))
    dataf = pd.read_excel(r'./station/未定义车站.xlsx', sheet_name='合并')
    dataf_unique = pd.DataFrame(dataf['站名'].unique())
    dataf_unique['定位'] = dataf_unique.agg(lambda x: get_provice_abbr(get_geoinfo(x, '')['province']), axis=1)
    print(dataf_unique)
    print(dataf_unique[dataf_unique['定位'] != ''].shape)
    dataf_unique.to_csv(r'./station/新站.csv')
    #lst = []
    #for item in dataf['站名']:
    #    lst.append(get_provice_abbr(get_geoinfo(item, '')['province']))
    #dataf['定位'] = lst
    #print(dataf)
    #dataf.to_csv(r'./station/已查询.csv', encoding='gbk')
    #dataf.to_csv(r'./station/完成查询.csv', encoding='gbk')