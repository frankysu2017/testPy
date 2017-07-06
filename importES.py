#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import random
import json

def import2ES():
    es = Elasticsearch("localhost:9200")
    data = {
        '@timestamp': datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+0800"),
        'http_code': '404',
        'count': random.randint(0, 10)
    }
    es.indices.create(index='newtest3')
    #es.index(index='newtest2', doc_type='docx', body={'name':'郭涛', 'id':'320103198106272078', 'sex':'male', 'age': 36})
    res = es.search(index='newtest2')
    print(res['hits']['hits'][0]['_source']['name'])

def createData():
    with open(r'c:/test/idata.txt', 'w+') as f:
        for i in range(100000):
            f.write('{"Name":"郭涛", "ID":"320103198106272078", "Sex":"male", "Age": 36, "Ethnic": "汉族"}\n')
    with open(r'c:/test/idata.txt', 'r') as f:
        textarr = []
        for line in f:
            textarr.append(line)
    #print(len(textarr))
    es = Elasticsearch("localhost:9200")
    actions = [
        {
            "_op_type": "index",
            "_index": "huji",
            "_type": "testdata",
            "_source": d
        }
        for d in textarr
    ]
    t1 = (datetime.now())
    helpers.bulk(es, actions)
    t2 = datetime.now()
    print(len(actions), t2-t1)
    res = es.search(index='huji')
    print(res['hits']['hits'][:10])

if __name__ == '__main__':
    createData()