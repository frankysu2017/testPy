#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from clickhouse_driver.client import Client

if __name__ == '__main__':
    client = Client(host='localhost', user='default', database='default', password='Qwerzxcv123')
    '''
    print(client.execute('show databases'))
    client.execute('USE default')
    print(client.execute('SHOW TABLES'))
    client.execute('DROP TABLE IF EXISTS test')
    client.execute('CREATE TABLE test (x Int32, y Int32, str String) ENGINE = Memory')
    client.execute('INSERT INTO test (x, y, str) VALUES', [(1, 2, "aaa"), (2, 2, "bbb")])
    client.execute('INSERT INTO test (x) VALUES', [[200]])
    print(client.execute('SELECT sum(y) FROM test'))
    print(type(client.execute('SELECT * FROM test')))
    print(client.execute('SELECT * FROM test'))
    '''
    client.execute('INSERT INTO linkedin', r'c:\19.txt')