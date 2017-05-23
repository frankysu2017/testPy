#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
利用高德地图api实现地址和经纬度的转换
我的高德key: 895d8c6afa27ba2b57dd757ab490e16d
'''
import requests

def geocode(city, address):
    parameters = {'address': address, 'city': city, 'key': '895d8c6afa27ba2b57dd757ab490e16d'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    answer = response.json()
    return answer

if __name__=='__main__':
    city = input('请输入城市：\n')
    address = input('请输入地址：\n')
    address = city + address
#    city = '北京'
#    address = '万寿路5号院'
    j_geo = geocode(city, address)
    arr_geo = []
    arr_geo.append(j_geo['geocodes'][0]['formatted_address'])   #标准化地址
    arr_geo.append(j_geo['geocodes'][0]['province'])            #省
    arr_geo.append(j_geo['geocodes'][0]['city'])                #市
    arr_geo.append(j_geo['geocodes'][0]['district'])            #区
    arr_geo.append(j_geo['geocodes'][0]['location'].split(',')[0])  #经度
    arr_geo.append(j_geo['geocodes'][0]['location'].split(',')[1])  #纬度
    t_geo = tuple(arr_geo)
    print('"%s","%s","%s","%s","%s","%s"' %t_geo)
    print(j_geo)
