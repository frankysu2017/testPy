#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    try:
#连接MySQL服务器：
        conn = pymysql.connect(host = 'localhost',
                               port = 3306,
                               user = 'hsiaoguo',
                               passwd = 'Qwerzxcv123',
                               db = 'test')
        cur = conn.cursor()
#对数据库进行操作
        QQdf = pd.read_sql("select QQacc, UNIX_TIMESTAMP(Qlog) as Qlog from qlog order by Qlog;", conn)
        grouped = QQdf.groupby(QQdf['QQacc'])
        arr_diff = []
        qindex = []
        for QQ, subgroup in grouped:
            QQlog = list(subgroup['Qlog'])
            QQlog.sort()
            QQlog_diff = list((map(lambda x: x[1] - x[0], zip(QQlog[0:len(QQlog)], QQlog[1:len(QQlog)+1]))))
            arr_diff.append(QQlog_diff)
            qindex.append(QQ)
        df_diff = pd.DataFrame(arr_diff, index = qindex).T
        df_diff.describe().to_csv('c:/工具/test.csv', encoding='utf-8')
        df_diff.boxplot()
        plt.show()
#关闭数据库
        cur.close()
        conn.close()
#打印MySQL错误
    except pymysql.Error as e:
        print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
