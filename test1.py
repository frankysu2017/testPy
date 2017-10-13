#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from matplotlib import pyplot as plt
from collections import Counter

def test1():
    names = ["Hero", "Dunn", "Sue", "Chi", "Thor", "Clive", "Hicks", "Devin", "Kate", "Klein"]
    users = []
    for id, name in enumerate(names):
        user = {}
        user["id"] = id
        user["name"] = name
        user["friends"] = []
        users.append(user)
    friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
    for i, j in friendships:
        users[i]['friends'].append(users[j]['id'])
        users[j]['friends'].append(users[i]['id'])
    num_friends_by_id = [(user['id'], len(user['friends'])) for user in users]
    num_friends_by_id.sort(key=lambda x:x[1], reverse=True)
    print(num_friends_by_id)

def test2():
    print('function test2 starts running!\n--------------------------------------------\n')
    grades = [random.randrange(0,100) for _ in range(100)]
    decile = lambda grade: grade // 10 * 10
    histogram = Counter(decile(grade) for grade in grades)
    plt.bar([x for x in histogram.keys()], histogram.values(), 8)
    plt.axis([-5, 105, 0, 20])
    plt.xticks([10 * i for i in range(11)])
    plt.xlabel('十分相')
    plt.ylabel('学生数')
    plt.title('考试分数分布图')
    plt.show()
    print('---------------------------------------------\nfunction test2 ends running!')

if __name__ == '__main__':
    test2()