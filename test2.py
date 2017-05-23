#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas
import time

with open('C:\\test\\testdate.txt', 'r+') as f:
    arr = f.readline().split(';')
    t3 = time.strptime(arr[3], '%d-%b-%y')
    t4 = time.strftime('%Y-%m-%d %H:%M:%S', t3)
    print(t4)