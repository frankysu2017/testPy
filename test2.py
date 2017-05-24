#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas
import time

with open('C:\\test\\testdate.txt', 'r+') as f:
    for line in f:
        arr = line.split(';')
        try:
            t3 = time.strptime(arr[3], '%d-%b-%y')
            t4 = time.strftime('%Y-%m-%d %H:%M:%S', t3)
            print(t4)
        except:
            print('error encounter an invalid date: %s' %arr[3])
