#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

def getData(filename):
    ferr = open(r'/Users/junie/Documents/twdata/error.txt', 'w', encoding='utf8')
    arr = []
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            l = line.split('#*#')
            if len(l) == 44:
                arr.append(l)
            else:
                ferr.write(line)
    col = [''] * 44
    col[0] = 'serial num'
    col[1] = 'flight num'
    col[2] = 'time1'
    col[3] = 'passport num'
    col[4] = 'unknown1'
    col[5] = 'family name'
    col[6] = 'first name'
    col[7] = 'unknown2'
    col[8] = 'sex'
    col[9] = 'birthdate'
    col[10] = 'nation?'
    col[11] = 'unknown3'
    col[12] = 'unknown4'
    col[13] = 'unknown5'
    col[14] = 'unknown6'
    col[15] = 'unknown7'
    col[16] = 'unknown8'
    col[17] = 'unknown9'
    col[18] = 'unknown10'
    col[19] = 'unknown11'
    col[20] = 'unknown12'
    col[21] = 'unknown13'
    col[22] = 'unknown14'
    col[23] = 'validty date'
    col[24] = 'unknown15'
    col[25] = 'unknown16'
    col[26] = 'unknown17'
    col[27] = 'unknown18'
    col[28] = 'unknown19'
    col[29] = 'time2'
    col[30] = 'time3'
    col[31] = 'unknown20'
    col[32] = 'unknown21'
    col[33] = 'unknown22'
    col[34] = 'unknown23'
    col[35] = 'unknown24'
    col[36] = 'english name'
    col[37] = 'unknown25'
    col[38] = 'time4'
    col[39] = 'unknown26'
    col[40] = 'unknown27'
    col[41] = 'datafile'
    col[42] = 'gettime'
    col[43] = 'return symbol'
    df = pd.DataFrame(arr, columns=col)
    df1 = df[df.time1 != '2018-12-12 03:00:00']
    print(df1.time1.max())
    print(df1.time1.min())
    print(len(df1))
    print(df1.gettime.max())
    print(df1.gettime.min())

if __name__ == '__main__':
    getData(r'/Users/junie/Documents/twdata/all.txt')