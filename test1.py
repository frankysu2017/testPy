#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

def printdict(dict1):
    for item in dict1:
        print(item)


if __name__ == '__main__':
    users  = [
        {"id": 0, "name": "Hero"},
        {"id": 1, "name": "Dunn"},
        {"id": 2, "name": "Sue"},
        {"id": 3, "name": "Chi"},
        {"id": 4, "name": "Thor"},
        {"id": 5, "name": "Clive"},
        {"id": 6, "name": "Hicks"},
        {"id": 7, "name": "Devin"},
        {"id": 8, "name": "Kate"},
        {"id": 9, "name": "Klein"}
    ]
    friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5,7), (6, 8), (7, 8), (8, 9)]
    for user in users:
        user["friends"] = []
    for i, j in friendships:
        users[i]["friends"].append(users[j]["id"])
        users[j]["friends"].append(users[i]["id"])
    #printdict(users)
    for i, j in enumerate(users):
        print("%s has %d friend(s)" %(j['name'], len(j['friends'])))

    str1="this is a pen, that is a pencil"
    list1 = str1.split(' ')
    list2 = list(str1)
    dict1 = Counter(list1)
    dict2 = Counter(list2)
    print(dict1)
    print(dict2)
    print(oct(27))
    print(int('0o33', 8))