#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#随机生成QQ的登录记录

import pymysql
import random
import time

if __name__ == "__main__":
    starttime = time.mktime(time.strptime('2017-1-1 0:0:0', '%Y-%m-%d %H:%M:%S'))
    endtime = time.mktime(time.strptime('2017-5-1 23:59:59', '%Y-%m-%d %H:%M:%S'))
    print('%d, %d' %(starttime, endtime))
    try:
#连接MySQL服务器：
        conn = pymysql.connect(host = 'localhost',
                               port = 3306,
                               user = 'hsiaoguo',
                               passwd = 'Qwerzxcv123',
                               db = 'test')
        cur = conn.cursor()
#对数据库进行操作
        createSQL = 'CREATE TABLE IF NOT EXISTS `qlog` (`QQacc`  varchar(255) NULL ,`Qlog`  datetime NULL );'
        cur.execute(createSQL)
        SQL = ''
        QQ_list = ['QQ0', 'QQ1', 'QQ2', 'QQ3', 'QQ4', 'QQ5', 'QQ6', 'QQ7', 'QQ8', 'QQ9']
        for i in range(10000):
            index = random.randint(0, 9)
            logtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(random.uniform(starttime, endtime)))
#            print('%d: QQ account is %s @ %s' %(i, QQ_list[index], logtime))
            SQL += "insert into `qlog` (`QQacc`, `Qlog`) VALUES('%s', '%s');\n" %(QQ_list[index], logtime)
        cur.execute(SQL)
        conn.commit()
#插入规律性登录的QQ10
        log_list = list(map(lambda x: time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1483200000 + 10454*x)), range(0,1000)))
        SQL_e = ''
        for i in range(len(log_list)):
            SQL_e += "insert into `qlog` (`QQacc`, `Qlog`) VALUES('%s', '%s');\n" %('QQ10', log_list[i])
        cur.execute(SQL_e)
        conn.commit()
#插入规律性登录的QQ10
        log_list = list(map(lambda x: time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1483200000 + 10434*x + random.uniform(0, 1800))), range(0,1000)))
        SQL_e = ''
        for i in range(len(log_list) - 1):
            SQL_e += "insert into `qlog` (`QQacc`, `Qlog`) VALUES('%s', '%s');\n" %('QQ11', log_list[i])
        cur.execute(SQL_e)
        cur.execute("insert into `qlog` (`QQacc`, `Qlog`) VALUES('QQ11','2016-12-27 21:0:0');")
        conn.commit()
#关闭数据库
        cur.close()
        conn.close()
#打印MySQL错误
    except pymysql.Error as e:
        print("Mysql Error %d: %s" % (e.args[0], e.args[1]))